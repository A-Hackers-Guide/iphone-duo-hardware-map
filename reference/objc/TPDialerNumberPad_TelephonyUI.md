# `TPDialerNumberPad`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPNumberPad`
- Protocols: `TPDialerKeypadProtocol`
- 3 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
B _playsSounds;
@"<TPDialerKeypadDelegate>" _delegate;
@"TPDialerSoundController" _soundController;
```

## Properties

```
@property (T@"TPDialerSoundController",&,V_soundController) soundController;
@property (TB,N,V_playsSounds) playsSounds;
@property (T@"<TPDialerKeypadDelegate>",V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TPDialerNumberPad dialerNumberPadFullCharacters];
+[TPDialerNumberPad dialerNumberPadNumericCharacters];
```

## Instance methods

```
-[TPDialerNumberPad buttonDown:];
-[TPDialerNumberPad buttonTapped:];
-[TPDialerNumberPad setDelegate:];
-[TPDialerNumberPad soundController];
-[TPDialerNumberPad delegate];
-[TPDialerNumberPad setSoundController:];
-[TPDialerNumberPad buttonUp:];
-[TPDialerNumberPad setPlaysSounds:];
-[TPDialerNumberPad buttonLongPressed:];
-[TPDialerNumberPad buttonUpOutside:];
-[TPDialerNumberPad highlightKeyAtIndex:];
-[TPDialerNumberPad indexForHighlightedKey];
-[TPDialerNumberPad playsSounds];
```
