<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ImAFish - simple_test</title>
</head>
<body>
    <?php
        if(isset($_POST['submit'])) {
            echo 'Username "' . $_POST['username'] . '" and password "' . $_POST['password'] . '" saved to database!';
        }
    ?>
    <form action="request.php" method="post">
        <label for="username">Username</label>
        <input id="username" type="text" name="username" value="">

        <label for="password">Password</label>
        <input id="password" type="password" name="password" value="">

        <input type="submit" name="submit" value="Submit!">
    </form>
</body>
</html>
