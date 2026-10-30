# `DSTouchIDController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSOBWelcomeController`
- Protocols: `BiometricKitUIEnrollResultDelegate`, `LARatchetViewControllerDelegate`, `DSController`
- 7 instance variables, 7 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"BiometricKitIdentity" _identity;
@"UIBarButtonItem" _cancelLeftNavigationItem;
B _enrollComplete;
@"LARatchetViewController" _ratchetVC;
@"<DSNavigationDelegate>" _delegate;
@"OBBoldTrayButton" _boldButton;
@"BiometricKitUIEnrollViewController" _enrollController;
```

## Properties

```
@property (T@"BiometricKitUIEnrollViewController",&,N,V_enrollController) enrollController;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (T@"OBBoldTrayButton",&,N,V_boldButton) boldButton;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSTouchIDController isTouchIDEnrolled];
+[DSTouchIDController hasMultipleFingerprints];
```

## Instance methods

```
-[DSTouchIDController init];
-[DSTouchIDController dealloc];
-[DSTouchIDController viewDidLoad];
-[DSTouchIDController setDelegate:];
-[DSTouchIDController setBoldButton:];
-[DSTouchIDController delegate];
-[DSTouchIDController boldButton];
-[DSTouchIDController ratchetViewController:didFinishWithResult:error:];
-[DSTouchIDController enrollResult:bkIdentity:];
-[DSTouchIDController beginEnrollment];
-[DSTouchIDController _cancelLeftNavigationItem];
-[DSTouchIDController _userDidTapCancelButton:];
-[DSTouchIDController addNavigationItems];
-[DSTouchIDController deleteIdentity];
-[DSTouchIDController enrollController];
-[DSTouchIDController enrollTouchID];
-[DSTouchIDController resetTouchID];
-[DSTouchIDController restartEnrollment];
-[DSTouchIDController setEnrollController:];
-[DSTouchIDController shouldShowWithCompletion:];
-[DSTouchIDController startRatchetEvalInPresentationContext:];
-[DSTouchIDController updateTouchIDPaneConfiguration];
```
