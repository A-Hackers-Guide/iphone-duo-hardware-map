# `SBDashBoardTraitsAwareAppHostingViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CSTraitsAwareOrientedAppHosting`
- 5 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _lastKnownWindowScene;
@"<SBApplicationHosting>" _appHosting;
@"TRAParticipant" _traitsParticipant;
@"SBTraitsSceneParticipantDelegate" _traitsParticipantDelegate;
@"SBTraitsOrientedContentViewController" _orientedContentViewController;
```

## Properties

```
@property (T@"TRAParticipant",&,N,V_traitsParticipant) traitsParticipant;
@property (T@"SBTraitsSceneParticipantDelegate",&,N,V_traitsParticipantDelegate) traitsParticipantDelegate;
@property (T@"SBTraitsOrientedContentViewController",&,N,V_orientedContentViewController) orientedContentViewController;
@property (T@"<SBApplicationHosting>",W,N,V_appHosting) appHosting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardTraitsAwareAppHostingViewController dealloc];
-[SBDashBoardTraitsAwareAppHostingViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBDashBoardTraitsAwareAppHostingViewController viewWillLayoutSubviews];
-[SBDashBoardTraitsAwareAppHostingViewController traitsParticipant];
-[SBDashBoardTraitsAwareAppHostingViewController setTraitsParticipant:];
-[SBDashBoardTraitsAwareAppHostingViewController _acquireTraitsParticipantOnWindowSceneIfNecessary:];
-[SBDashBoardTraitsAwareAppHostingViewController _hostedAppViewController];
-[SBDashBoardTraitsAwareAppHostingViewController _hostedSceneHandle];
-[SBDashBoardTraitsAwareAppHostingViewController _invalidateTraitsParticipant];
-[SBDashBoardTraitsAwareAppHostingViewController _referenceBoundsForBounds:];
-[SBDashBoardTraitsAwareAppHostingViewController appHosting];
-[SBDashBoardTraitsAwareAppHostingViewController hostedSceneHandle];
-[SBDashBoardTraitsAwareAppHostingViewController initWithAppHosting:];
-[SBDashBoardTraitsAwareAppHostingViewController orientedContentViewController];
-[SBDashBoardTraitsAwareAppHostingViewController sceneDidAttach];
-[SBDashBoardTraitsAwareAppHostingViewController sceneWasDestroyed];
-[SBDashBoardTraitsAwareAppHostingViewController setAppHosting:];
-[SBDashBoardTraitsAwareAppHostingViewController setContentViewBounds:];
-[SBDashBoardTraitsAwareAppHostingViewController setOrientedContentViewController:];
-[SBDashBoardTraitsAwareAppHostingViewController setTraitsParticipantDelegate:];
-[SBDashBoardTraitsAwareAppHostingViewController traitsParticipantDelegate];
```
