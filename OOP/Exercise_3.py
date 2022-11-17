from datetime import datetime, timezone, timedelta
from time import sleep

class Timer:
    tz = timezone.utc

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self):
        if self._time_start is None:
            raise TimeError('Timer must be started before it can be stopped.')
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started.')
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped.')
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before an elapsed time can be calculated.')
        if self._time_end is None:
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            elapsed_time = self._time_end - self._time_start
        return elapsed_time.total_seconds()

t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f'Start Time: {t1.start_time}')
print(f'End Time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')
