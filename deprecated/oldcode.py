# if call == 1:
#     API_URL = 'https://api.linkedin.com/v2/learningActivityReports?aggregationCriteria.primary=INDIVIDUAL&q=criteria&start=0&startedAt=1639112400000&count=1000&timeOffset.duration=1&timeOffset.unit=WEEK'
#     r = requests.get(API_URL, headers=HEADERS).json()
#     for item in r['elements']:
#         email = item['learnerDetails']['email']
#         uid = item['learnerDetails']['uniqueUserId']
#
#         days_active = item['activities'][0]['engagementValue']
#         seconds_viewed = item['activities'][1]['engagementValue']
#
#         video_views = item['activities'][18]['engagementValue']
#         video_completions = item['activities'][19]['engagementValue']
#
#         article_views = item['activities'][2]['engagementValue']
#         article_completions = item['activities'][3]['engagementValue']
#
#         audio_views = item['activities'][4]['engagementValue']
#         audio_completions = item['activities'][5]['engagementValue']
#
#         book_views = item['activities'][6]['engagementValue']
#         book_completions = item['activities'][7]['engagementValue']
#
#         learning_collection_views = item['activities'][8]['engagementValue']
#         learning_collection_completions = item['activities'][9]['engagementValue']
#
#         course_views = item['activities'][10]['engagementValue']
#         course_completions = item['activities'][11]['engagementValue']
#
#         document_views = item['activities'][12]['engagementValue']
#         document_completions = item['activities'][13]['engagementValue']
#
#         event_views = item['activities'][14]['engagementValue']
#         event_completions = item['activities'][15]['engagementValue']
#
#         learning_path_views = item['activities'][16]['engagementValue']
#         learning_path_completions = item['activities'][17]['engagementValue']
#
#         record = {'email': email,
#                   'uid': uid,
#                   'days_active': days_active,
#                   'seconds_viewed': seconds_viewed,
#                   'video_views': video_views,
#                   'video_completions': video_completions,
#                   'article_views': article_views,
#                   'article_completions': article_completions,
#                   'audio_views': audio_views,
#                   'audio_completions': audio_completions,
#                   'book_views': book_views,
#                   'book_completions': book_completions,
#                   'learning_collection_views': learning_collection_views,
#                   'learning_collection_completions': learning_collection_completions,
#                   'course_views': course_views,
#                   'course_completions': course_completions,
#                   'document_views': document_views,
#                   'document_completions': document_completions,
#                   'event_views': event_views,
#                   'event_completions': event_completions,
#                   'learning_path_views': learning_path_views,
#                   'learning_path_completions': learning_path_completions}
#         payload.append(record)
#     return json.dumps(payload)
#
# if call == 2:
#     API_URL = 'https://api.linkedin.com/v2/learningActivityReports?q=criteria&count=1&startedAt=1641044200000&timeOffset.unit=DAY&timeOffset.duration=7&aggregationCriteria.primary=ACCOUNT&contentSource=ALL_SOURCES'
#     r = requests.get(API_URL, headers=HEADERS).json()
#     for item in r['elements']:
#         email = item['learnerDetails']['email']
#         content = item['contentDetails']['name']
#         uid = item['learnerDetails']['uniqueUserId']
#         asset_type = item['activities'][0]['assetType']
#         seconds_viewed = item['activities'][0]['engagementValue']
#         progress_percentage = item['activities'][1]['engagementValue']
#         created_date = date.today()
#         record = {'email': email, 'uid': uid, 'content': content, 'asset_type': asset_type,
#                   'seconds_viewed': seconds_viewed, 'progress_percentage': progress_percentage,
#                   'created_date': created_date}
#         payload.append(record)
#     return json.dumps(payload)
