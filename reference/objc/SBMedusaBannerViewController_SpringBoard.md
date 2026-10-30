# `SBMedusaBannerViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BNPresentable`
- 4 instance variables, 14 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"PLPillView" _pillView;
q _type;
q _orientation;
q _peekConfiguration;
```

## Properties

```
@property (Tq,?,R,N) presentableBehavior;
@property (T@"<BNPresentableContext>",?,W,N) presentableContext;
@property (T@"NSSet",?,R,C,N) preferredBackgroundActivitiesToSuppress;
@property (TB,?,R,N,GisDraggingDismissalEnabled) draggingDismissalEnabled;
@property (TB,?,R,N,GisDraggingInteractionEnabled) draggingInteractionEnabled;
@property (TB,?,R,N,GisTouchOutsideDismissalEnabled) touchOutsideDismissalEnabled;
@property (T@"UIViewController",?,R,N) viewController;
@property (Tq,?,R,N) presentableType;
@property (T@"NSString",R,C,N) requesterIdentifier;
@property (T@"NSString",R,C,N) requestIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMedusaBannerViewController requestIdentifier];
-[SBMedusaBannerViewController viewDidLoad];
-[SBMedusaBannerViewController requesterIdentifier];
-[SBMedusaBannerViewController viewController];
-[SBMedusaBannerViewController _bannerView];
-[SBMedusaBannerViewController initWithType:orientation:peekConfiguration:];
```
