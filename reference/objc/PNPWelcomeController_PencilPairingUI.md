# `PNPWelcomeController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBWelcomeController`
- 9 instance variables, 10 properties, 29 instance methods, 5 class methods

## Instance variables

```
? delegate;
q controllerType;
q buttonType;
q deviceType;
? trayButtons;
Q features;
B usesExtraContentInsets;
B showsIcon;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 navigationTitleLabel;
```

## Properties

```
@property (T@"<_TtP15PencilPairingUI28PNPWelcomeControllerDelegate_>",N,W,Vdelegate) delegate;
@property (Tq,N,VcontrollerType) controllerType;
@property (Tq,N,VbuttonType) buttonType;
@property (Tq,N,VdeviceType) deviceType;
@property (T@"NSArray",N,C) trayButtons;
@property (TQ,N,Vfeatures) features;
@property (TB,N,VusesExtraContentInsets) usesExtraContentInsets;
@property (TB,N,VshowsIcon) showsIcon;
@property (TB,N,R) isRTL;
@property (T{UIEdgeInsets=dddd},N) additionalSafeAreaInsets;
```

## Class methods

```
+[PNPWelcomeController bundleImageNamed:renderingMode:];
+[PNPWelcomeController _controllerWithType:buttonType:deviceType:delegate:];
+[PNPWelcomeController bundleImageNamed:];
+[PNPWelcomeController controllerWithType:buttonType:deviceType:delegate:];
+[PNPWelcomeController controllerWithType:buttonType:deviceType:features:delegate:];
```

## Instance methods

```
-[PNPWelcomeController features];
-[PNPWelcomeController setDeviceType:];
-[PNPWelcomeController setFeatures:];
-[PNPWelcomeController buttonType];
-[PNPWelcomeController initWithTitle:detailText:icon:];
-[PNPWelcomeController deviceType];
-[PNPWelcomeController viewDidLayoutSubviews];
-[PNPWelcomeController additionalSafeAreaInsets];
-[PNPWelcomeController _canShowWhileLocked];
-[PNPWelcomeController setDelegate:];
-[PNPWelcomeController setButtonType:];
-[PNPWelcomeController delegate];
-[PNPWelcomeController initWithTitle:detailText:symbolName:contentLayout:];
-[PNPWelcomeController initWithTitle:detailText:icon:contentLayout:];
-[PNPWelcomeController isRTL];
-[PNPWelcomeController setAdditionalSafeAreaInsets:];
-[PNPWelcomeController setShowsIcon:];
-[PNPWelcomeController showsIcon];
-[PNPWelcomeController buttonPressed:];
-[PNPWelcomeController controllerType];
-[PNPWelcomeController setControllerType:];
-[PNPWelcomeController bundleImageNamed:renderingMode:];
-[PNPWelcomeController setTrayButtons:];
-[PNPWelcomeController bundleImageNamed:];
-[PNPWelcomeController refreshNavigationTitleLayout];
-[PNPWelcomeController setControllerType:buttonType:deviceType:delegate:];
-[PNPWelcomeController setUsesExtraContentInsets:];
-[PNPWelcomeController trayButtons];
-[PNPWelcomeController usesExtraContentInsets];
```
