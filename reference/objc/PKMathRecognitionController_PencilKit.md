# `PKMathRecognitionController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _currentItems;
@"NSDictionary" _changeMap;
@"NSDictionary" _stableIdentifierMap;
@"NSDictionary" _sortIndexMap;
@"NSDictionary" _expressionMap;
@"NSDictionary" _shouldSolveMap;
@"NSArray" _currentMathRecognitionItems;
@"NSArray" _delayedItems;
d _updateItemsDelay;
{?="delegateSupportsLatestTimestampForUserInteraction"b1"delegateSupportsSolveStateChanged"b1"delegateSupportsDidEraseStrokes"b1} _delegateFlags;
B _isRTL;
@"<PKMathRecognitionControllerDelegate>" _delegate;
@"PKRecognitionSessionManager" __sessionManager;
```

## Properties

```
@property (T@"<PKMathRecognitionControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[PKMathRecognitionController initWithDelegate:];
-[PKMathRecognitionController init];
-[PKMathRecognitionController reset];
-[PKMathRecognitionController setDelegate:];
-[PKMathRecognitionController delegate];
-[PKMathRecognitionController didEraseStrokes:];
-[PKMathRecognitionController processDelayedItemsIfNecessary];
-[PKMathRecognitionController sendDelayedItems];
```
