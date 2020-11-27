import os

if 'LPDECR_BENCH' in os.environ and os.environ['LPDECR_BENCH'] == '1':
    print('[LPDecrypter] Benchmarking has been enabled')
    from profilehooks import profile, timecall
else:
    def profile(func):
        return func

    def timecall(func):
        return func
