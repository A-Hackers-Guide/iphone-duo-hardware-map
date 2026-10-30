# `SBAppResizingSession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWorkspaceApplicationSceneTransitionContextDelegate`, `SBLayoutStateTransitionSceneEntityFrameProvider`
- 13 instance variables, 17 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"SBWindowSceneManager" _windowSceneManager;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"SBSAppResizingAssertionStorage" _storage;
@"SBSUIApplicationResizeConstraintHelper" _constraintHelper;
@"NSHashTable" _observers;
{CGSize="width"d"height"d} _reportedResolvedSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _transactionFrame;
@"SBInAppStatusBarHiddenAssertion" _hideStatusBarAssertion;
@"SBWindowScene" _monitoredWindowScene;
@"<SBLayoutStateTransitionSceneEntityFrameProvider>" _sceneEntityFrameProviderToRestore;
q _state;
@"NSSet" _windowScenes;
@"<SBAppResizingSessionDelegate>" _delegate;
```

## Properties

```
@property (T@"SBSAppResizingAssertionStorage",R,N,V_storage) storage;
@property (T{CGSize=dd},N) preferredSize;
@property (TB,R,N) isActive;
@property (TB,R,N) isValid;
@property (T@"SBDeviceApplicationSceneHandle",R,N) sceneHandle;
@property (T{CGSize=dd},R,N) resolvedSize;
@property (T@"NSSet",R,N,V_windowScenes) windowScenes;
@property (T@"NSUUID",R,N) uniqueIdentifier;
@property (T@"NSString",R,C,N) displayUniqueId;
@property (Td,R,N) resizingCornerRadius;
@property (T{CGSize=dd},R,N) minimumPossibleSize;
@property (T{CGSize=dd},R,N) maximumPossibleSize;
@property (T@"<SBAppResizingSessionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppResizingSession prepareForDisplay];
-[SBAppResizingSession sceneHandle];
-[SBAppResizingSession removeObserver:];
-[SBAppResizingSession dealloc];
-[SBAppResizingSession applicationTransitionContext:frameForApplicationSceneEntity:];
-[SBAppResizingSession layoutStateForApplicationTransitionContext:];
-[SBAppResizingSession uniqueIdentifier];
-[SBAppResizingSession storage];
-[SBAppResizingSession addObserver:];
-[SBAppResizingSession invalidate];
-[SBAppResizingSession setDelegate:];
-[SBAppResizingSession previousLayoutStateForApplicationTransitionContext:];
-[SBAppResizingSession windowScenes];
-[SBAppResizingSession resolvedSize];
-[SBAppResizingSession isValid];
-[SBAppResizingSession activate];
-[SBAppResizingSession delegate];
-[SBAppResizingSession setPreferredSize:];
-[SBAppResizingSession isActive];
-[SBAppResizingSession setSceneHandle:];
-[SBAppResizingSession preferredSize];
-[SBAppResizingSession displayUniqueId];
-[SBAppResizingSession commitResolvedSize:];
-[SBAppResizingSession maximumPossibleSize];
-[SBAppResizingSession minimumPossibleSize];
-[SBAppResizingSession resizingCornerRadius];
-[SBAppResizingSession _calculateResolvedSize:constraintHelper:];
-[SBAppResizingSession _effectivePreferredSize];
-[SBAppResizingSession _updateMinSize:maxSize:notify:];
-[SBAppResizingSession _updateResolvedSize];
-[SBAppResizingSession _updateToFrame:completion:];
-[SBAppResizingSession canReceiveSceneHandle:];
-[SBAppResizingSession initWithWindowSceneManager:displayUniqueId:monitoredWindowScene:resizingCornerRadius:];
-[SBAppResizingSession monitoredWindowScene];
-[SBAppResizingSession sceneEntityFrameForWorkspaceEntity:inLayoutState:];
```
