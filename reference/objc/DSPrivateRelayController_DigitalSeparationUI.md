# `DSPrivateRelayController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSOBWelcomeController`
- Protocols: `DSController`
- 4 instance variables, 8 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"OBBoldTrayButton" _enableButton;
@"OBLinkTrayButton" _linkButton;
Q _proxyServiceStatus;
```

## Properties

```
@property (T@"OBBoldTrayButton",&,N,V_enableButton) enableButton;
@property (T@"OBLinkTrayButton",&,N,V_linkButton) linkButton;
@property (TQ,N,V_proxyServiceStatus) proxyServiceStatus;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSPrivateRelayController initialize];
```

## Instance methods

```
-[DSPrivateRelayController init];
-[DSPrivateRelayController viewDidLoad];
-[DSPrivateRelayController setDelegate:];
-[DSPrivateRelayController delegate];
-[DSPrivateRelayController linkButton];
-[DSPrivateRelayController setLinkButton:];
-[DSPrivateRelayController enableButton];
-[DSPrivateRelayController enableButtonTitle];
-[DSPrivateRelayController learnMorePressed];
-[DSPrivateRelayController privateRelayDetailText];
-[DSPrivateRelayController proxyServiceStatus];
-[DSPrivateRelayController setEnableButton:];
-[DSPrivateRelayController setPrivateRelayEnabledWithHandler:];
-[DSPrivateRelayController setProxyServiceStatus:];
-[DSPrivateRelayController shouldShowWithCompletion:];
-[DSPrivateRelayController turnOnPrivateRelay];
```
