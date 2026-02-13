function savePhoto() {
    const url = document.getElementById('photoUrl').value;
    if(!url) return;
    db.ref('vault').push({
        data: "IMAGE_LINK: " + url,
        timestamp: Date.now()
    });
    document.getElementById('photoUrl').value = "";
    alert("Babita's Photo Link Saved!");
}
