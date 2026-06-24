import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='SMIT@1706',
        database='desktop_tracker'
    )
    return conn

def save_user(name, email, token):

    connection = get_connection()

    if connection is None:
        return

    try:

        cursor = connection.cursor()

        query = """
        INSERT INTO users(name, email, token)
        VALUES(%s, %s, %s)
        """

        cursor.execute(
            query,
            (name, email, token)
        )

        connection.commit()

    except Exception as e:
        print("Save User Error:", e)

    finally:
        connection.close()

def save_screenshot(
    filename,
    filepath
):

    connection = get_connection()

    if connection is None:
        return

    try:

        cursor = connection.cursor()

        query = """
        INSERT INTO screenshots
        (
            filename,
            filepath,
            timestamp
        )
        VALUES
        (
            %s,
            %s,
            NOW()
        )
        """

        cursor.execute(
            query,
            (
                filename,
                filepath
            )
        )

        connection.commit()

    except Exception as e:
        print(
            "Screenshot Save Error:",
            e
        )

    finally:
        connection.close()    

def save_activity_log(
    session_id,
    keyboard_events,
    mouse_events
):
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO activity_logs
            (
                session_id,
                keyboard_events,
                mouse_events,
                timestamp
            )
            VALUES
            (
                %s,
                %s,
                %s,
                NOW()
            )
            """

        cursor.execute(
            query,
            (   
                session_id,
                keyboard_events,
                mouse_events
            )
        )

        connection.commit()

    except Exception as e:
        print(
            "Activity Save Error:",
            e
        )

    finally:
        connection.close()

def get_pending_activities():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM activity_logs
            WHERE synced = FALSE
        """)

        return cursor.fetchall()

    finally:
        connection.close()

def get_pending_screenshots():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM screenshots
            WHERE synced = FALSE
        """)

        return cursor.fetchall()

    finally:
        connection.close()

def mark_activity_synced(activity_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE activity_logs
            SET synced = TRUE
            WHERE id = %s
            """,
            (activity_id,)
        )

        connection.commit()

    finally:
        connection.close()

def mark_screenshot_synced(
    screenshot_id
):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE screenshots
            SET synced = TRUE
            WHERE id = %s
            """,
            (screenshot_id,)
        )

        connection.commit()

    finally:
        connection.close()


def create_session():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO tracking_sessions
            (
                status,
                start_time
            )
            VALUES
            (
                'running',
                NOW()
            )
            """
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()

def stop_session(session_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE tracking_sessions
            SET
                status = 'stopped',
                end_time = NOW()
            WHERE id = %s
            """,
            (session_id,)
        )

        connection.commit()

    finally:

        connection.close()