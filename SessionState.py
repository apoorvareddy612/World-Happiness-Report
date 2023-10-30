# import streamlit.report_thread as ReportThread
# from streamlit.server.server import Server
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
from streamlit.web.server import Server
from streamlit.runtime import get_instance

class SessionState():
    def __init__(self, **kwargs):
        
        for key, val in kwargs.items():
            setattr(self, key, val)


def get(**kwargs):
    runtime = get_instance()
    session_id = get_script_run_ctx().session_id #.get_report_ctx()
 #    session_info = Server._get_session_info(session_id) #.get_current()
    session_info = runtime._session_mgr.get_session_info(session_id)

    if session_info is None:
        raise RuntimeError('Could not get Streamlit session object.')

    this_session = session_info.session

    # Got the session object! Now let's attach some state into it.

    if not hasattr(this_session, '_custom_session_state'):
        this_session._custom_session_state = SessionState(**kwargs)

    return this_session._custom_session_state
