import settings

class CRIsoFile(settings.UserFilePath):
    """
    Locate the user's Custom Robo USA ISO file.
    """

    description = "Custom Robo USA ISO"
    copy_to = None

class CRSettings(settings.Group):
    iso_file: CRIsoFile = CRIsoFile(CRIsoFile.copy_to)