# `PKTextInputTargetState`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `PKTextInputDebugStateReporting`
- 15 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
B _nextCommitShouldHavePrecedingSeparator;
@"NSNumber" _elementRecognitionIdentifier;
@"CHTextInputQueryItem" _lastQueryItem;
@"PKTextInputHandwritingShot" _handwritingShot;
@"NSNumber" _writingSessionIdentifier;
@"NSString" _uncommittedPendingText;
@"NSString" _activePreviewText;
q _sessionCommitLength;
q _lastCommittedCharacterLevelPosition;
@"NSUUID" _inProgressGestureStrokeUUID;
d _inProgressGestureStartTimestamp;
d _lastUpdateTimestamp;
{_NSRange="location"Q"length"Q} _inProgressGestureInitialSelectedRange;
{_NSRange="location"Q"length"Q} _inProgressGestureSelectionRange;
{_NSRange="location"Q"length"Q} _inProgressGestureRangeToDelete;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputTargetState init];
-[PKTextInputTargetState description];
-[PKTextInputTargetState copyWithZone:];
-[PKTextInputTargetState reportDebugStateDescription:];
```
