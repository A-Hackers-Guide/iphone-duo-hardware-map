# `PKTextInputResultCommand`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
B _resultedInTargetChange;
B _hasPendingUncommittedChanges;
B _destinationFrameForAnimationMightMove;
B __applyIntermediateChange;
@"<PKTextInputResultCommandDelegate>" _delegate;
q _commandState;
@"CHTextInputQueryItem" _queryItem;
@"PKTextInputHandwritingShot" _handwritingShot;
@"PKTextInputElementContent" _targetElementContent;
@"PKTextInputTargetState" _initialInputTargetState;
q _immediateCommitType;
@"PKTextInputTargetState" _finalInputTargetState;
@"NSString" _committedText;
q _committedTokenColumnCount;
@"NSString" _commitReason;
@"PKTextInputTargetState" __inProgressInputTargetState;
{_NSRange="location"Q"length"Q} _affectedRange;
```

## Instance methods

```
-[PKTextInputResultCommand description];
```
