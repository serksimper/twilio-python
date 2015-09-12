from twilio.rest.taskrouter.client import TaskrouterClient
from twilio.rest.resources.task_router import (
    Activities,
    Events,
    Reservations,
    TaskQueues,
    Tasks,
    Workers,
    Workflows,
    Workspaces,
)


class TwilioTaskRouterClient(TaskrouterClient):
    """
    A client for accessing the Twilio TaskRouter API

    :param str account: Your Account SID from `your dashboard
        <https://twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://twilio.com/user/account>`_
    :param float timeout: The socket and read timeout for requests to Twilio
    """

    def __init__(self, *args, **kwargs):
        """
        Create a Twilio REST API client for task router.
        """
        super(TwilioTaskRouterClient, self).__init__(*args, **kwargs)
        self.base_uri = self.version_uri
        self.workspace_uri = "{0}/Workspaces".format(self.base_uri)

    def activities(self, workspace_sid):
        """
        Return a :class:`Activities` instance for the :class:`Activity`
        with the given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Activities(self.client, base_uri, self.auth, self.timeout)

    def events(self, workspace_sid):
        """
        Return a :class:`Events` instance for the :class:`Event` with the given
        workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Events(self.client, base_uri, self.auth, self.timeout)

    def reservations(self, workspace_sid, task_sid):
        """
        Return a :class:`Reservations` instance for the :class:`Reservation`
        with the given workspace_sid ans task_sid
        """
        base_uri = "{0}/{1}/Tasks/{2}".format(self.workspace_uri,
                                              workspace_sid, task_sid)
        return Reservations(self.client, base_uri, self.auth, self.timeout)

    def task_queues(self, workspace_sid):
        """
        Return a :class:`TaskQueues` instance for the :class:`TaskQueue` with
        the given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return TaskQueues(self.client, base_uri, self.auth, self.timeout)

    def tasks(self, workspace_sid):
        """
        Return a :class:`Tasks` instance for the :class:`Task` with the given
        workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Tasks(self.client, base_uri, self.auth, self.timeout)

    def workers(self, workspace_sid):
        """
        Return a :class:`Workers` instance for the :class:`Worker` with the
        given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Workers(self.client, base_uri, self.auth, self.timeout)

    def workflows(self, workspace_sid):
        """
        Return a :class:`Workflows` instance for the :class:`Workflow` with the
        given workspace_sid
        """
        base_uri = "{0}/{1}".format(self.workspace_uri, workspace_sid)
        return Workflows(self.client, base_uri, self.auth, self.timeout)