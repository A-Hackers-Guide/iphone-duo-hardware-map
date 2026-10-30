# `CAMProminentObjectManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"<CAMMetadataObjectResult>" _currentObject;
{CGPoint="x"d"y"d} _currentObjectPointOfInterest;
@"<CAMMetadataObjectResult>" _expiringObject;
@"<CAMMetadataObjectResult>" _candidateObject;
d _candidateTimestamp;
@"BCSDetectedCode" _currentlyParsingCode;
@"BCSAction" _previousAction;
@"BCSAction" _currentAction;
@"<CAMProminentObjectManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<CAMMetadataObjectResult>",R,N) currentObject;
@property (TB,R,N,GisCurrentObjectExpiring) currentObjectExpiring;
@property (T@"BCSAction",R,N) currentMachineReadableCodeAction;
@property (TQ,R,N) currentObjectType;
@property (T@"<CAMProminentObjectManagerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CAMProminentObjectManager reset];
-[CAMProminentObjectManager setDelegate:];
-[CAMProminentObjectManager delegate];
-[CAMProminentObjectManager currentObject];
-[CAMProminentObjectManager _beginExpiringCurrentObjectIfNeeded];
-[CAMProminentObjectManager _candidateObjectMatchingCurrentObject:];
-[CAMProminentObjectManager _expirationTimeForObjectType:];
-[CAMProminentObjectManager _handleExpiredObject:];
-[CAMProminentObjectManager _isMetadataObject:semanticallyEqualToMetadataObject:];
-[CAMProminentObjectManager _isPoint:equalToPoint:tolerance:];
-[CAMProminentObjectManager _mostSignificantObjectFromObjects:preferredObject:pointOfInterest:];
-[CAMProminentObjectManager _selectionDelayForNewObject:];
-[CAMProminentObjectManager _setCurrentMachineReadableCodeAction:];
-[CAMProminentObjectManager _setCurrentMachineReadableCodeAction:updatePreviousAction:];
-[CAMProminentObjectManager _setCurrentObject:forPointOfInterest:];
-[CAMProminentObjectManager _updateCurrentMRCActionWhenReady];
-[CAMProminentObjectManager _viewportBoundsForAspectCorrection];
-[CAMProminentObjectManager currentMachineReadableCodeAction];
-[CAMProminentObjectManager currentObjectType];
-[CAMProminentObjectManager isCurrentObjectExpiring];
-[CAMProminentObjectManager isCurrentObjectLikelyEqualToObject:];
-[CAMProminentObjectManager typeForMetadataObject:];
-[CAMProminentObjectManager updateWithCandidateObjects:];
```
