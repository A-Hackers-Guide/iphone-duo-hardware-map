# `CAMTimelapseDiskUtilities`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 26 class methods

## Class methods

```
+[CAMTimelapseDiskUtilities hasPendingWork];
+[CAMTimelapseDiskUtilities directoryPathForTimelapseUUID:];
+[CAMTimelapseDiskUtilities dummyFileName];
+[CAMTimelapseDiskUtilities dummyFilePathForTimelapseUUID:];
+[CAMTimelapseDiskUtilities fileNameForImageFrameIndex:];
+[CAMTimelapseDiskUtilities fileNameForImageVISIndex:];
+[CAMTimelapseDiskUtilities frameIndexFromImageFileName:];
+[CAMTimelapseDiskUtilities readFrameFilePathsForTimelapseUUID:];
+[CAMTimelapseDiskUtilities readSecondaryStateForTimelapseUUID:];
+[CAMTimelapseDiskUtilities readSortedStatesFromDiskMergeSecondaryState:];
+[CAMTimelapseDiskUtilities readStateForTimelapseUUID:mergeSecondaryState:];
+[CAMTimelapseDiskUtilities removeDummyFileForTimelapseUUID:];
+[CAMTimelapseDiskUtilities reserveDummyFileForTimelapseUUID:width:height:useHEVC:];
+[CAMTimelapseDiskUtilities secondaryStateFileName];
+[CAMTimelapseDiskUtilities secondaryStateFilePathForTimelapseUUID:];
+[CAMTimelapseDiskUtilities sortedArrayFromFilePathDictionary:reverse:];
+[CAMTimelapseDiskUtilities stateFileName];
+[CAMTimelapseDiskUtilities stateFilePathForTimelapseUUID:];
+[CAMTimelapseDiskUtilities timelapseDirectoryPath];
+[CAMTimelapseDiskUtilities timelapseDirectoryPathCreateIfNeeded:];
+[CAMTimelapseDiskUtilities timelapseUUIDsOnDisk];
+[CAMTimelapseDiskUtilities updateSecondaryStateForMovieWriteAttemptForTimelapseUUID:];
+[CAMTimelapseDiskUtilities updateSecondaryStateForTimelapseUUID:forStateReadSuccessfully:];
+[CAMTimelapseDiskUtilities updateSecondaryStateForTimelapseUUID:withStopReasons:stopTime:];
+[CAMTimelapseDiskUtilities writeSecondaryStateToDisk:forTimelapseUUID:];
+[CAMTimelapseDiskUtilities writeStateToDisk:createDirectoryIfNeeded:];
```
