# `DSReviewAccessController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSOBWelcomeController`
- Protocols: `DSController`
- 2 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"DSAlternateDeviceAccessManager" _accessManager;
```

## Properties

```
@property (T@"DSAlternateDeviceAccessManager",&,N,V_accessManager) accessManager;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSReviewAccessController init];
-[DSReviewAccessController viewDidLoad];
-[DSReviewAccessController setDelegate:];
-[DSReviewAccessController delegate];
-[DSReviewAccessController goToSafetyCheck];
-[DSReviewAccessController _descriptionTextForDeviceNameList:format:];
-[DSReviewAccessController accessManager];
-[DSReviewAccessController cancelReset];
-[DSReviewAccessController presentErrorAlert:];
-[DSReviewAccessController presentMoreOptions];
-[DSReviewAccessController resetAllDeviceAccess];
-[DSReviewAccessController setAccessManager:];
```
