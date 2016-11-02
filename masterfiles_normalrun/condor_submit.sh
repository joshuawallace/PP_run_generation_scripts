#For submitting

executable     = /u/joshuajw/PlanetProject/mercury/mercury7
universe       = standard
log            = condorlog.log
output         = condorstdout.out
error          = condorerror.out
should_transfer_files = IF_NEEDED
when_to_transfer_output = ON_EXIT
notify_user   = joshuawallace800@gmail.com
notification  = Always
queue
