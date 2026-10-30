# `SBDodgingResolverViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBChainableModifierDelegate`
- 12 instance variables, 16 properties, 50 instance methods, 0 class methods

## Instance variables

```
B _dispatchingEvent;
B _needsModelUpdate;
B _needsLayout;
@"SBRootDodgingLayerModifier" _rootModifier;
@"SBDodgingModel" _model;
@"NSMutableDictionary" _itemsForIdentifiers;
q _contentOrientation;
@"NSMutableArray" _eventQueue;
@"NSMutableSet" _itemsNeedingUpdate;
@"NSMutableSet" _itemsNeedingNonAnimatedUpdate;
@"UILabel" _debugOverlay;
Q _lastUpdateTimeNS;
```

## Properties

```
@property (T@"SBRootDodgingLayerModifier",&,N,V_rootModifier) rootModifier;
@property (T@"SBDodgingModel",&,N,V_model) model;
@property (T@"NSMutableDictionary",&,N,V_itemsForIdentifiers) itemsForIdentifiers;
@property (Tq,N,V_contentOrientation) contentOrientation;
@property (T@"NSMutableArray",&,N,V_eventQueue) eventQueue;
@property (TB,N,GisDispatchingEvent,V_dispatchingEvent) dispatchingEvent;
@property (T@"NSMutableSet",&,N,V_itemsNeedingUpdate) itemsNeedingUpdate;
@property (T@"NSMutableSet",&,N,V_itemsNeedingNonAnimatedUpdate) itemsNeedingNonAnimatedUpdate;
@property (TB,N,V_needsModelUpdate) needsModelUpdate;
@property (TB,N,V_needsLayout) needsLayout;
@property (T@"UILabel",&,N,V_debugOverlay) debugOverlay;
@property (TQ,N,V_lastUpdateTimeNS) lastUpdateTimeNS;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDodgingResolverViewController model];
-[SBDodgingResolverViewController eventQueue];
-[SBDodgingResolverViewController setEventQueue:];
-[SBDodgingResolverViewController interfaceOrientation];
-[SBDodgingResolverViewController setModel:];
-[SBDodgingResolverViewController setDebugOverlay:];
-[SBDodgingResolverViewController contentOrientation];
-[SBDodgingResolverViewController setContentOrientation:];
-[SBDodgingResolverViewController viewDidLoad];
-[SBDodgingResolverViewController initWithNibName:bundle:];
-[SBDodgingResolverViewController rootModifier];
-[SBDodgingResolverViewController loadView];
-[SBDodgingResolverViewController _updateLayoutIfNeeded];
-[SBDodgingResolverViewController setNeedsLayout:];
-[SBDodgingResolverViewController needsLayout];
-[SBDodgingResolverViewController debugOverlay];
-[SBDodgingResolverViewController _updateItemsIfNeeded];
-[SBDodgingResolverViewController _setNeedsLayout];
-[SBDodgingResolverViewController _performEventResponse:];
-[SBDodgingResolverViewController invalidateItem:];
-[SBDodgingResolverViewController _dispatchNextEventIfNeededAndHandleResponse];
-[SBDodgingResolverViewController _dispatchOrAppendEvent:];
-[SBDodgingResolverViewController _handleEventResponse:];
-[SBDodgingResolverViewController _performInvalidationResponse:];
-[SBDodgingResolverViewController _performScheduleEventResponse:];
-[SBDodgingResolverViewController _setAllItemsNeedUpdate];
-[SBDodgingResolverViewController _setItemNeedsUpdate:];
-[SBDodgingResolverViewController _setNeedsModelUpdate];
-[SBDodgingResolverViewController _updateItemIfNeeded:];
-[SBDodgingResolverViewController _updateLayoutWithItemIdentifier:completion:];
-[SBDodgingResolverViewController _updateModelIfNeeded];
-[SBDodgingResolverViewController addItemWithIdentifier:view:initialCenter:initialSize:delegate:];
-[SBDodgingResolverViewController contentViewBounds];
-[SBDodgingResolverViewController isDispatchingEvent];
-[SBDodgingResolverViewController itemsForIdentifiers];
-[SBDodgingResolverViewController itemsNeedingNonAnimatedUpdate];
-[SBDodgingResolverViewController itemsNeedingUpdate];
-[SBDodgingResolverViewController lastUpdateTimeNS];
-[SBDodgingResolverViewController needsModelUpdate];
-[SBDodgingResolverViewController performTransitionFromOrientation:toOrientation:animated:mutationBlock:];
-[SBDodgingResolverViewController preferenceForIdentifier:];
-[SBDodgingResolverViewController setDispatchingEvent:];
-[SBDodgingResolverViewController setItemNeedsUpdate:animated:];
-[SBDodgingResolverViewController setItemsForIdentifiers:];
-[SBDodgingResolverViewController setItemsNeedingNonAnimatedUpdate:];
-[SBDodgingResolverViewController setItemsNeedingUpdate:];
-[SBDodgingResolverViewController setLastUpdateTimeNS:];
-[SBDodgingResolverViewController setNeedsModelUpdate:];
-[SBDodgingResolverViewController setRootModifier:];
-[SBDodgingResolverViewController spaceBetweenIdentifiers];
```
