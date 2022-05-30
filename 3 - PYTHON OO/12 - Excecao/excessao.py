class IxiMariaEAgoraError(Exception):
    pass


def testar():
    raise IxiMariaEAgoraError('Errado')

testar()