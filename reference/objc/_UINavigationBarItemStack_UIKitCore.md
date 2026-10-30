# `_UINavigationBarItemStack`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 16 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _previousItems;
@"NSMutableArray" _items;
i _state;
@"<_UINavigationItemChangeObserver>" _changeObserver;
@"_UINavigationBarTransitionAssistant" _transitionAssistant;
```

## Properties

```
@property (T@"<_UINavigationItemChangeObserver>",W,N,V_changeObserver) changeObserver;
@property (Ti,R,N,V_state) state;
@property (T@"_UINavigationBarTransitionAssistant",R,N,V_transitionAssistant) transitionAssistant;
@property (T@"_UINavigationBarItemStackEntry",R,N) topEntry;
@property (T@"_UINavigationBarItemStackEntry",R,N) backEntry;
@property (T@"_UINavigationBarItemStackEntry",R,N) previousTopEntry;
@property (T@"_UINavigationBarItemStackEntry",R,N) previousBackEntry;
@property (T@"UINavigationItem",R,N) topItem;
@property (T@"UINavigationItem",R,N) backItem;
@property (T@"UINavigationItem",R,N) previousTopItem;
@property (T@"UINavigationItem",R,N) previousBackItem;
@property (T@"NSArray",R,C,N) items;
@property (Tq,R,N) itemCount;
@property (TB,R,N,GisPushingOrPopping) pushingOrPopping;
@property (TB,R,N,GisPushing) pushing;
@property (TB,R,N,GisPopping) popping;
```

## Instance methods

```
-[_UINavigationBarItemStack isPushingOrPopping];
-[_UINavigationBarItemStack itemCount];
-[_UINavigationBarItemStack reverseIterateEntries:];
-[_UINavigationBarItemStack iterateEntries:];
-[_UINavigationBarItemStack _shim_pushNestedNavigationItem:];
-[_UINavigationBarItemStack pushItem:withTransitionAssistant:];
-[_UINavigationBarItemStack _synchronizeChangeObservers];
-[_UINavigationBarItemStack previousBackEntry];
-[_UINavigationBarItemStack init];
-[_UINavigationBarItemStack _effectiveDisplayModeForItem:inStack:];
-[_UINavigationBarItemStack stackItemsAreEqualTo:];
-[_UINavigationBarItemStack _completeTransition];
-[_UINavigationBarItemStack items];
-[_UINavigationBarItemStack effectiveDisplayModeForItemInCurrentStack:];
-[_UINavigationBarItemStack topItem];
-[_UINavigationBarItemStack backItem];
-[_UINavigationBarItemStack popItemWithTransitionAssistant:];
-[_UINavigationBarItemStack previousBackItem];
-[_UINavigationBarItemStack _cleanupTransitionAssistant];
-[_UINavigationBarItemStack completeOperation];
-[_UINavigationBarItemStack _shim_popNestedNavigationItem];
-[_UINavigationBarItemStack previousTopItem];
-[_UINavigationBarItemStack beginInteractiveTransition];
-[_UINavigationBarItemStack setItems:withTransitionAssistant:];
-[_UINavigationBarItemStack effectiveBarCompressionBehaviorForItemInCurrentStack:];
-[_UINavigationBarItemStack topEntry];
-[_UINavigationBarItemStack description];
-[_UINavigationBarItemStack previousTopEntry];
-[_UINavigationBarItemStack isPushing];
-[_UINavigationBarItemStack isPopping];
-[_UINavigationBarItemStack transitionAssistant];
-[_UINavigationBarItemStack backEntry];
-[_UINavigationBarItemStack setChangeObserver:];
-[_UINavigationBarItemStack changeObserver];
-[_UINavigationBarItemStack _updateChangeObserversFor:];
-[_UINavigationBarItemStack effectiveDisplayModeForItemInPreviousStack:];
-[_UINavigationBarItemStack endInteractiveTransition];
-[_UINavigationBarItemStack iterateItems:];
-[_UINavigationBarItemStack state];
-[_UINavigationBarItemStack initWithItems:];
-[_UINavigationBarItemStack _prepareTransitionWithAssistant:];
-[_UINavigationBarItemStack cancelOperation];
```
