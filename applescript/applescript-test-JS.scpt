JsOsaDAS1.001.00bplist00�Vscript_// Display Notification

var app = Application.currentApplication()
app.includeStandardAdditions = true

app.displayNotification("All graphics have been converted.", {
    withTitle: "My Graphic Processing Script",
    subtitle: "Processing is complete.",
    soundName: "Frog"
})
