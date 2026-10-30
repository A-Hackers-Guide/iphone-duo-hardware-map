# `SBContinuousExposeIdentifierSlideModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 7 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isWaitingToPrepareLayout;
B _isWaitingToBeginAnimation;
@"NSString" _uniqueAnimationIdentifier;
@"NSString" _continuousExposeIdentifier;
@"NSArray" _previousContinuousExposeIdentifiersInSwitcher;
@"NSArray" _previousContinuousExposeIdentifiersInStrip;
Q _direction;
```

## Properties

```
@property (T@"NSString",R,C,N,V_continuousExposeIdentifier) continuousExposeIdentifier;
@property (T@"NSArray",R,C,N,V_previousContinuousExposeIdentifiersInSwitcher) previousContinuousExposeIdentifiersInSwitcher;
@property (T@"NSArray",R,C,N,V_previousContinuousExposeIdentifiersInStrip) previousContinuousExposeIdentifiersInStrip;
@property (TQ,R,N,V_direction) direction;
```

## Instance methods

```
-[SBContinuousExposeIdentifierSlideModifier scaleForIndex:];
-[SBContinuousExposeIdentifierSlideModifier anchorPointForIndex:];
-[SBContinuousExposeIdentifierSlideModifier continuousExposeIdentifier];
-[SBContinuousExposeIdentifierSlideModifier animationAttributesForLayoutElement:];
-[SBContinuousExposeIdentifierSlideModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBContinuousExposeIdentifierSlideModifier handleTimerEvent:];
-[SBContinuousExposeIdentifierSlideModifier frameForIndex:];
-[SBContinuousExposeIdentifierSlideModifier direction];
-[SBContinuousExposeIdentifierSlideModifier handleContinuousExposeIdentifiersChangedEvent:];
-[SBContinuousExposeIdentifierSlideModifier _beginAnimation];
-[SBContinuousExposeIdentifierSlideModifier _performBlockWithIdentifiersInSwitcher:identifiersInStrip:block:];
-[SBContinuousExposeIdentifierSlideModifier _waitingToAnimateReason];
-[SBContinuousExposeIdentifierSlideModifier _waitingToPrepareLayoutReason];
-[SBContinuousExposeIdentifierSlideModifier initWithContinuousExposeIdentifier:previousContinuousExposeIdentifiersInSwitcher:previousContinuousExposeIdentifiersInStrip:direction:];
-[SBContinuousExposeIdentifierSlideModifier previousContinuousExposeIdentifiersInStrip];
-[SBContinuousExposeIdentifierSlideModifier previousContinuousExposeIdentifiersInSwitcher];
```
