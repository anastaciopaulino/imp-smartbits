from datetime import datetime

# function to generate the gallary's file path
def gallery_directory_path(instance, filename):
    
    # file will be uploaded to MEDIA_ROOT/gallery/images/<filename>
    dt = datetime.now()
    filename = str(dt.strftime("IMG_%H%M%S%d%y%m")) + \
        '.' + str(filename).split('.')[-1]
    return 'gallary/images/{0}' .format(filename)


# function to generate the testemonial's file path
def testemonial_directory_path(instance, filename):
    
    # file will be uploaded to MEDIA_ROOT/testimonial/images/<filename>
    dt = datetime.now()
    filename = str(dt.strftime("IMG_%H%M%S%d%y%m")) + \
        '.' + str(filename).split('.')[-1]
    return 'testemonials/images/{0}' .format(filename)