# `DSFaceIDController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSOBWelcomeController`
- Protocols: `BKUIPearlEnrollControllerDelegate`, `LARatchetViewControllerDelegate`, `DSController`
- 6 instance variables, 9 properties, 20 instance methods, 3 class methods

## Instance variables

```
@"LARatchetViewController" _ratchetVC;
@"<DSNavigationDelegate>" _delegate;
@"LAContext" _authContext;
@"UINavigationController" _faceIDEnrollmentNavigationController;
@"OBBoldTrayButton" _boldButton;
@"DSBiometricManager" _biometricManager;
```

## Properties

```
@property (T@"LAContext",&,N,V_authContext) authContext;
@property (T@"UINavigationController",&,N,V_faceIDEnrollmentNavigationController) faceIDEnrollmentNavigationController;
@property (T@"OBBoldTrayButton",&,N,V_boldButton) boldButton;
@property (T@"DSBiometricManager",&,N,V_biometricManager) biometricManager;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSFaceIDController hasAlternateAppearance];
+[DSFaceIDController isPearlEnrolled];
+[DSFaceIDController supportsPearl];
```

## Instance methods

```
-[DSFaceIDController init];
-[DSFaceIDController viewDidLoad];
-[DSFaceIDController authContext];
-[DSFaceIDController setDelegate:];
-[DSFaceIDController setBoldButton:];
-[DSFaceIDController delegate];
-[DSFaceIDController boldButton];
-[DSFaceIDController setAuthContext:];
-[DSFaceIDController ratchetViewController:didFinishWithResult:error:];
-[DSFaceIDController _didTapCancelButton];
-[DSFaceIDController pearlEnrollController:finishedEnrollWithError:];
-[DSFaceIDController beginFaceIDEnrollment];
-[DSFaceIDController biometricManager];
-[DSFaceIDController faceIDEnrollmentNavigationController];
-[DSFaceIDController resetFaceID];
-[DSFaceIDController setBiometricManager:];
-[DSFaceIDController setFaceIDEnrollmentNavigationController:];
-[DSFaceIDController shouldShowWithCompletion:];
-[DSFaceIDController startRatchetEvalInPresentationContext:];
-[DSFaceIDController updateFaceIDPaneConfiguration];
```
