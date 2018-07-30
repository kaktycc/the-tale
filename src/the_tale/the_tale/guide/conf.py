
import smart_imports

smart_imports.all()

settings = dext_app_settings.app_settings('GUIDE',
                                          DEVELOPMENT_PLANS_URL='https://docs.the-tale.org/ru/latest/plans.html',
                                          DEVELOPMENT_FORUM='https://the-tale.org/forum/subcategories/3',
                                          HTTP_API_DOCUMENTATION='https://docs.the-tale.org/ru/latest/external_api/index.html')
