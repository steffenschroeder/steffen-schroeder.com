Title: Syntax Usage
Date: 2018-09-20
Summary: This is an internal page
Status: Draft
Category: Development
Tags: Internal, pelican

# This internal page shows some useful syntax usages

and this is the text

    :::python
    def clean():
        """Remove generated files"""
         if os.path.isdir(DEPLOY_PATH):
            shutil.rmtree(DEPLOY_PATH)
            os.makedirs(DEPLOY_PATH)
            # Hello World

And now in java

    :::java
    public void open(int row, int column) {
  Field fieldToOpen = board.getField(row, column);
  if (!fieldToOpen.isOpen()) {
   fieldToOpen.open();
   if (fieldToOpen.isMine()) {
    openAllFields();
    nofifyGameLost();

   } else if (gameWon()) {
    notifyGameWon();
   }
   notifyBoardChanged();
  }
 }

See the ```notifyBoardChanged()``` - wonderful
