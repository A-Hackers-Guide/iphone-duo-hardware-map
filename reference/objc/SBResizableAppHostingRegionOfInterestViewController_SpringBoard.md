# `SBResizableAppHostingRegionOfInterestViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBAppResizingCoordinatorObserver`, `SBAppResizingSessionObserver`
- 2 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"UIView" _regionOfInterestView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _regionOfInterestFrame;
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
-[SBResizableAppHostingRegionOfInterestViewController initWithView:];
-[SBResizableAppHostingRegionOfInterestViewController viewDidLoad];
-[SBResizableAppHostingRegionOfInterestViewController viewWillLayoutSubviews];
-[SBResizableAppHostingRegionOfInterestViewController resizingCoordinator:didUpdateActiveSession:];
-[SBResizableAppHostingRegionOfInterestViewController resizingSession:didBeginResizingTransactionWithFrame:];
```
