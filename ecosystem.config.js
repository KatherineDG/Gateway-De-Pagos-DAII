module.exports = {
    apps: [
      {
        name: "pagos",
        script: "manage.py",
        args: "runserver 0.0.0.0:8000",
        interpreter: "python3",
      },
    ],
  };