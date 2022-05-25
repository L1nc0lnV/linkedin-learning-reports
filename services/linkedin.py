from datetime import date
import requests
import json
from settings.linkedin import LinkedInConfig as settings
from db.db import _write_to_sql as wrsql

class LinkedinService:
    payload = []
    li = settings()

    for asset in li.ASSET_TYPE:
        eof = False
        API_URL = f'https://api.linkedin.com/v2/learningActivityReports?start={li.PAGE_START}&count={li.PAGE_COUNT}&' \
                  'aggregationCriteria.primary=INDIVIDUAL&' \
                  'aggregationCriteria.secondary=CONTENT&q=criteria&start=0&contentSource=ALL_SOURCES&' \
                  f'assetType={asset}&startedAt={li.MEASURE_PERIOD_START}&' \
                  f'timeOffset.duration={li.MEASURE_PERIOD_LOOKAHEAD}&timeOffset.unit={li.MEASURE_PERIOD}'

        while not eof:
            r = requests.get(API_URL, headers=li.HEADERS).json()
            for record in r['elements']:
                email = record['learnerDetails']['email']
                content = record['contentDetails']['name'].lstrip().replace('"', '')
                uid = record['learnerDetails']['uniqueUserId']
                content_id = record['contentDetails']['contentUrn'][-7:]
                if 'lyndaCourse' in record['contentDetails']['contentUrn']:
                    content_id_idx = (len(record['contentDetails']['contentUrn']) - record['contentDetails'][
                        'contentUrn'].find('lyndaCourse:')) * -1
                elif 'lyndaLearningPath' in record['contentDetails']['contentUrn']:
                    content_id_idx = (len(record['contentDetails']['contentUrn']) - record['contentDetails'][
                        'contentUrn'].find('lyndaLearningPath:')) * -1
                elif 'learningCustomContent' in record['contentDetails']['contentUrn']:
                    content_id_idx = (len(record['contentDetails']['contentUrn']) - record['contentDetails'][
                        'contentUrn'].find('learningCustomContent:')) * -1
                elif 'Recommended Content for Learning Paths' in record['contentDetails']['name']:
                    content_id_idx = (len(record['contentDetails']['contentUrn']) - record['contentDetails'][
                        'contentUrn'].find('lyndaLearningCollection:')) * -1
                content_id = record['contentDetails']['contentUrn'][content_id_idx:].replace(')', '')
                asset_type = record['activities'][0]['assetType']
                seconds_viewed = record['activities'][0]['engagementValue']
                if len(record['activities']) < 2:
                    progress_percentage = 0
                else:
                    progress_percentage = record['activities'][1]['engagementValue']
                created_date = str(date.today())
                record = {'uid': uid, 'email': email, 'content': content, 'content_id': content_id,
                          'asset_type': asset_type, 'seconds_viewed': seconds_viewed,
                          'progress_percentage': progress_percentage, 'created_date': created_date}
                payload.append(record)
            if len(r['paging']['links']) != 0:
                for links in r['paging']['links']:
                    if links['rel'] == 'next':
                        API_URL = 'https://api.linkedin.com' + links['href']
                    else:
                        eof = True
            else:
                eof = True

    wrsql(li.DBTABLE, json.dumps(payload))



