# `UIDocument`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UINavigationItemRenameDelegateInternal`, `UINavigationItemRenameDelegate`, `NSFilePresenter`, `NSProgressReporting`
- 24 instance variables, 20 properties, 121 instance methods, 7 class methods

## Instance variables

```
@"NSUserActivity" _currentUserActivity;
@"NSLock" _activityContinuationLock;
@"NSURL" _fileURL;
@"NSString" _fileBookmark;
@"NSString" _fileType;
@"NSString" _localizedName;
@"NSUndoManager" _undoManager;
@"NSDate" _fileModificationDate;
@"NSObject<OS_dispatch_queue>" _fileAccessQueue;
@"NSObject<OS_dispatch_queue>" _openingQueue;
@"NSObject<OS_dispatch_semaphore>" _fileAccessSemaphore;
@"NSOperationQueue" _filePresenterQueue;
@ _differenceDueToRecentChanges;
@ _differenceSincePreservingPreviousVersion;
@ _differenceSinceSaving;
@"NSTimer" _autosavingTimer;
d _lastSaveTime;
d _lastPreservationTime;
@ _versionWithoutRecentChanges;
@"NSMutableArray" _versions;
@ _alertPresenter;
@ _progressSubscriber;
@"NSMutableSet" _progresses;
{__docFlags="inClose"b1"isOpen"b1"inOpen"b1"inRevert"b1"isAutosavingBecauseOfTimer"b1"versionWithoutRecentChangesIsNotLastOpened"b1"ignoreUndoAndRedoNotifications"b1"editingTemporarilyDisabled"b1"editingDisabledDueToPermissions"b1"isRegisteredAsFilePresenter"b1"movingFile"b1"savingError"b1"inConflict"b1"needToStopAccessingSecurityScopedResource"b1"replacedDefaultUserActivity"b1} _docFlags;
```

## Properties

```
@property (T@"NSDocumentDifferenceSize",R,N,V_differenceDueToRecentChanges) differenceDueToRecentChanges;
@property (T@"NSDocumentDifferenceSize",R,N,V_differenceSincePreservingPreviousVersion) differenceSincePreservingPreviousVersion;
@property (T@"NSDocumentDifferenceSize",R,N,V_differenceSinceSaving) differenceSinceSaving;
@property (T@"NSURL",R) fileURL;
@property (T@"NSString",R,C) localizedName;
@property (T@"NSString",R,C) fileType;
@property (T@"NSDate",C) fileModificationDate;
@property (TQ,R) documentState;
@property (T@"NSProgress",R) progress;
@property (T@"NSUndoManager",&) undoManager;
@property (TB,R,N) hasUnsavedChanges;
@property (T@"NSString",R,N) savingFileType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSURL",R,C) presentedItemURL;
@property (T@"NSOperationQueue",R,&) presentedItemOperationQueue;
@property (T@"NSURL",?,R,C) primaryPresentedItemURL;
@property (T@"NSSet",?,R) observedPresentedItemUbiquityAttributes;
```

## Class methods

```
+[UIDocument _autosavingTimerDidFireSoContinue:];
+[UIDocument _customizationOfError:withDescription:recoverySuggestion:recoveryAttempter:];
+[UIDocument _documentWithContentsOfFileURL:error:];
+[UIDocument _fileModificationDateForURL:];
+[UIDocument _finishWritingToURL:withTemporaryDirectoryURL:newContentsURL:afterSuccess:];
+[UIDocument _typeForContentsOfURL:error:];
+[UIDocument _url:matchesURL:];
```

## Instance methods

```
-[UIDocument _applicationDidBecomeActive:];
-[UIDocument documentState];
-[UIDocument restoreUserActivityState:];
-[UIDocument updateUserActivityState:];
-[UIDocument fileModificationDate];
-[UIDocument closeWithCompletionHandler:];
-[UIDocument setUndoManager:];
-[UIDocument fileURL];
-[UIDocument userActivity];
-[UIDocument init];
-[UIDocument setUserActivity:];
-[UIDocument undoManager];
-[UIDocument initWithFileURL:];
-[UIDocument relinquishPresentedItemToWriter:];
-[UIDocument presentedItemOperationQueue];
-[UIDocument dealloc];
-[UIDocument accommodatePresentedSubitemDeletionAtURL:completionHandler:];
-[UIDocument localizedName];
-[UIDocument progress];
-[UIDocument relinquishPresentedItemToReader:];
-[UIDocument savePresentedItemChangesWithCompletionHandler:];
-[UIDocument accommodatePresentedItemDeletionWithCompletionHandler:];
-[UIDocument presentedItemURL];
-[UIDocument _applicationWillResignActive:];
-[UIDocument _performBlockOnMainThread:];
-[UIDocument presentedItemDidMoveToURL:];
-[UIDocument description];
-[UIDocument _setFileURL:];
-[UIDocument fileType];
-[UIDocument hasUnsavedChanges];
-[UIDocument setFileType:];
-[UIDocument openWithCompletionHandler:];
-[UIDocument presentedSubitemDidAppearAtURL:];
-[UIDocument presentedSubitemDidChangeAtURL:];
-[UIDocument presentedItemDidChange];
-[UIDocument presentedItemDidGainVersion:];
-[UIDocument presentedItemDidLoseVersion:];
-[UIDocument presentedItemDidResolveConflictVersion:];
-[UIDocument presentedItemHasUnsavedChangesWithCompletionHandler:];
-[UIDocument presentedSubitemAtURL:didGainVersion:];
-[UIDocument presentedSubitemAtURL:didLoseVersion:];
-[UIDocument presentedSubitemAtURL:didMoveToURL:];
-[UIDocument presentedSubitemAtURL:didResolveConflictVersion:];
-[UIDocument _autosaveWithCompletionHandler:];
-[UIDocument _changeWasDone:];
-[UIDocument _isOpen];
-[UIDocument writeContents:andAttributes:safelyToURL:forSaveOperation:error:];
-[UIDocument _hasSavingError];
-[UIDocument _setEditingTemporarilyDisabled:];
-[UIDocument _setInConflict:];
-[UIDocument writeContents:toURL:forSaveOperation:originalContentsURL:error:];
-[UIDocument _autosavingCompletedSuccessfully:];
-[UIDocument _autosavingDelay];
-[UIDocument _changeWasRedone:];
-[UIDocument _changeWasUndone:];
-[UIDocument _coordinateWritingItemAtURL:error:byAccessor:];
-[UIDocument _defaultUserActivityForActivityType:];
-[UIDocument _defaultUserActivityType];
-[UIDocument _fileOpeningQueue];
-[UIDocument _finishSavingToURL:forSaveOperation:changeCount:];
-[UIDocument _hasUnsavedChanges];
-[UIDocument _isEditingDisabledDueToPermissions];
-[UIDocument _isEditingTemporarilyDisabled];
-[UIDocument _isInConflict];
-[UIDocument _isInOpen];
-[UIDocument _isUbiquitous];
-[UIDocument _lockFileAccessQueueAndPerformBlock:];
-[UIDocument _navigationItemFileURLForRenaming:];
-[UIDocument _performBlock:synchronouslyOnQueue:];
-[UIDocument _performBlockSynchronouslyOnMainThread:];
-[UIDocument _presentableFileNameForSaveOperation:url:];
-[UIDocument _progressPublished:];
-[UIDocument _progressUnpublished:];
-[UIDocument _readingProgressForURL:];
-[UIDocument _registerAsFilePresenterIfNecessary];
-[UIDocument _releaseUndoManager];
-[UIDocument _rescheduleAutosaving];
-[UIDocument _saveUnsavedChangesWithCompletionHandler:];
-[UIDocument _scheduleAutosaving];
-[UIDocument _scheduleAutosavingAfterDelay:reset:];
-[UIDocument _sendStateChangedNotification];
-[UIDocument _setEditingDisabledDueToPermissions:];
-[UIDocument _setHasSavingError:];
-[UIDocument _setInOpen:];
-[UIDocument _setOpen:];
-[UIDocument _setUserActivity:];
-[UIDocument _shouldAllowWritingInResponseToPresenterMessage];
-[UIDocument _unlockFileAccessQueue];
-[UIDocument _unregisterAsFilePresenterIfNecessary];
-[UIDocument _updateConflictState];
-[UIDocument _updateDefaultUserActivityBecomingCurrent:];
-[UIDocument _updateLastUsedDate];
-[UIDocument _updateLocalizedName];
-[UIDocument _updatePermissionsState:];
-[UIDocument _updateUserActivityState:];
-[UIDocument _userActivity];
-[UIDocument _writingProgressForURL:indeterminate:];
-[UIDocument autosaveWithCompletionHandler:];
-[UIDocument changeCountTokenForSaveOperation:];
-[UIDocument contentsForType:error:];
-[UIDocument differenceDueToRecentChanges];
-[UIDocument differenceSincePreservingPreviousVersion];
-[UIDocument differenceSinceSaving];
-[UIDocument disableEditing];
-[UIDocument enableEditing];
-[UIDocument fileAttributesToWriteToURL:forSaveOperation:error:];
-[UIDocument fileNameExtensionForType:saveOperation:];
-[UIDocument finishedHandlingError:recovered:];
-[UIDocument handleError:userInteractionPermitted:];
-[UIDocument loadFromContents:ofType:error:];
-[UIDocument navigationItem:didEndRenamingWithTitle:];
-[UIDocument performAsynchronousFileAccessUsingBlock:];
-[UIDocument presentedItemDidMoveToWritableLocation];
-[UIDocument readFromURL:error:];
-[UIDocument revertToContentsOfURL:completionHandler:];
-[UIDocument saveToURL:forSaveOperation:completionHandler:];
-[UIDocument savingFileType];
-[UIDocument setFileModificationDate:];
-[UIDocument updateChangeCount:];
-[UIDocument updateChangeCountWithToken:forSaveOperation:];
-[UIDocument userInteractionNoLongerPermittedForError:];
```
