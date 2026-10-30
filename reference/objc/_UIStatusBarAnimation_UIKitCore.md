# `_UIStatusBarAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `_UIStatusBarPrioritized`
- 17 instance variables, 18 properties, 45 instance methods, 5 class methods

## Instance variables

```
B _delaysAnimatingItems;
B _delaysDependentItems;
B _enabled;
q _priority;
@"_UIStatusBarIdentifier" _displayItemIdentifier;
@"NSString" _identifier;
@"NSString" _exclusivityGroupIdentifier;
q _type;
@? _prepareBlock;
@"NSSet" _delayedItemIdentifiers;
@"NSSet" _delayedDisplayItemPlacements;
@"NSMutableArray" _subAnimations;
@"_UIStatusBarAnimation" _parentAnimation;
d _timeout;
@? _animationBlock;
@? _timeoutBlock;
@"NSMutableArray" _completionHandlers;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_subAnimations) subAnimations;
@property (T@"_UIStatusBarAnimation",W,N,V_parentAnimation) parentAnimation;
@property (Td,N,V_timeout) timeout;
@property (T@?,C,N,V_animationBlock) animationBlock;
@property (T@?,C,N,V_timeoutBlock) timeoutBlock;
@property (T@"NSMutableArray",&,N,V_completionHandlers) completionHandlers;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Tq,N,V_type) type;
@property (T@"NSSet",R,N) effectiveDelayedItemIdentifiers;
@property (T@"_UIStatusBarIdentifier",C,N,V_displayItemIdentifier) displayItemIdentifier;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_exclusivityGroupIdentifier) exclusivityGroupIdentifier;
@property (T@?,C,N,V_prepareBlock) prepareBlock;
@property (T@"NSSet",C,N,V_delayedItemIdentifiers) delayedItemIdentifiers;
@property (T@"NSSet",C,N,V_delayedDisplayItemPlacements) delayedDisplayItemPlacements;
@property (TB,N,V_delaysAnimatingItems) delaysAnimatingItems;
@property (TB,N,V_delaysDependentItems) delaysDependentItems;
@property (Tq,N,V_priority) priority;
```

## Class methods

```
+[_UIStatusBarAnimation initialize];
+[_UIStatusBarAnimation _addAnimations:toDispatchGroup:];
+[_UIStatusBarAnimation prepareAnimations:forStatusBar:];
+[_UIStatusBarAnimation _addAnimations:toPreparingAnimations:exclusiveAnimations:visitedDisplayItemIdentifiers:];
+[_UIStatusBarAnimation animationWithBlock:];
```

## Instance methods

```
-[_UIStatusBarAnimation priority];
-[_UIStatusBarAnimation addCompletionHandler:];
-[_UIStatusBarAnimation addTotalCompletionHandler:];
-[_UIStatusBarAnimation completionHandlers];
-[_UIStatusBarAnimation identifier];
-[_UIStatusBarAnimation displayItemIdentifier];
-[_UIStatusBarAnimation setParentAnimation:];
-[_UIStatusBarAnimation setAnimationBlock:];
-[_UIStatusBarAnimation parentAnimation];
-[_UIStatusBarAnimation animationBlock];
-[_UIStatusBarAnimation setDisplayItemIdentifier:];
-[_UIStatusBarAnimation setDelaysDependentItems:];
-[_UIStatusBarAnimation _dependentItemIdentifiersEnabledOnly:];
-[_UIStatusBarAnimation setDelayedDisplayItemPlacements:];
-[_UIStatusBarAnimation setPriority:];
-[_UIStatusBarAnimation _prepareForStatusBar:preparingAnimations:exclusiveAnimations:];
-[_UIStatusBarAnimation setCompletionHandlers:];
-[_UIStatusBarAnimation prepareBlock];
-[_UIStatusBarAnimation addTimeout:withHandler:];
-[_UIStatusBarAnimation performForStatusBar:];
-[_UIStatusBarAnimation subAnimations];
-[_UIStatusBarAnimation delayedDisplayItemPlacements];
-[_UIStatusBarAnimation setDelayedItemIdentifiers:];
-[_UIStatusBarAnimation timeout];
-[_UIStatusBarAnimation isEnabled];
-[_UIStatusBarAnimation setIdentifier:];
-[_UIStatusBarAnimation delaysAnimatingItems];
-[_UIStatusBarAnimation setType:];
-[_UIStatusBarAnimation setTimeout:];
-[_UIStatusBarAnimation type];
-[_UIStatusBarAnimation exclusivityGroupIdentifier];
-[_UIStatusBarAnimation setEnabled:];
-[_UIStatusBarAnimation delaysDependentItems];
-[_UIStatusBarAnimation setTimeoutBlock:];
-[_UIStatusBarAnimation setPrepareBlock:];
-[_UIStatusBarAnimation description];
-[_UIStatusBarAnimation addSubAnimation:forDisplayItemWithIdentifier:];
-[_UIStatusBarAnimation timeoutBlock];
-[_UIStatusBarAnimation copyWithZone:];
-[_UIStatusBarAnimation cancel];
-[_UIStatusBarAnimation delayedItemIdentifiers];
-[_UIStatusBarAnimation setSubAnimations:];
-[_UIStatusBarAnimation setDelaysAnimatingItems:];
-[_UIStatusBarAnimation setExclusivityGroupIdentifier:];
-[_UIStatusBarAnimation effectiveDelayedItemIdentifiers];
```
