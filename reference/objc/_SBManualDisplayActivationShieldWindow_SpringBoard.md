# `_SBManualDisplayActivationShieldWindow`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRootWindow`
- 7 instance variables, 1 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"UIButton" _activationButton;
@"UIButton" _powerOffButton;
@"SBWindowScene" _sbWindowScene;
@"<BSInvalidatable>" _disableSystemGestureAssertion;
@"BLSAssertion" _alwaysOnDisabledAssertion;
@"BSCompoundAssertion" _disableButtonsAssertions;
B _shieldActive;
```

## Properties

```
@property (TB,N,GisShieldActive,V_shieldActive) shieldActive;
```

## Class methods

```
+[_SBManualDisplayActivationShieldWindow isRequired];
+[_SBManualDisplayActivationShieldWindow _isSecure];
+[_SBManualDisplayActivationShieldWindow _currentShieldWindow];
```

## Instance methods

```
-[_SBManualDisplayActivationShieldWindow layoutSubviews];
-[_SBManualDisplayActivationShieldWindow _sbWindowScene];
-[_SBManualDisplayActivationShieldWindow pointInside:withEvent:];
-[_SBManualDisplayActivationShieldWindow _supportedInterfaceOrientationsForRootViewController];
-[_SBManualDisplayActivationShieldWindow _activateWindowScene];
-[_SBManualDisplayActivationShieldWindow _ensureAllWindowScenesHaveActivationWindows];
-[_SBManualDisplayActivationShieldWindow _otherWindows];
-[_SBManualDisplayActivationShieldWindow _powerOffDisplay];
-[_SBManualDisplayActivationShieldWindow initWithSBWindowScene:];
-[_SBManualDisplayActivationShieldWindow isShieldActive];
-[_SBManualDisplayActivationShieldWindow setShieldActive:];
-[_SBManualDisplayActivationShieldWindow startShielding];
-[_SBManualDisplayActivationShieldWindow stopShielding];
```
