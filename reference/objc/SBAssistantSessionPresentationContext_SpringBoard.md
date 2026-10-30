# `SBAssistantSessionPresentationContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSMutableCopying`
- 7 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _assistantPresented;
B _keyboardVisible;
B _allowsHDRContentBelow;
B _wantsDeemphasizedBackdrop;
B _assistantAccessoryPresented;
B _effectivelyVisionModality;
@"SiriPresentationOptions" _siriPresentationOptions;
```

## Properties

```
@property (TB,N,GisAssistantPresented,V_assistantPresented) assistantPresented;
@property (T@"SiriPresentationOptions",&,N,V_siriPresentationOptions) siriPresentationOptions;
@property (TB,N,GisKeyboardVisible,V_keyboardVisible) keyboardVisible;
@property (TB,N,V_allowsHDRContentBelow) allowsHDRContentBelow;
@property (TB,N,V_wantsDeemphasizedBackdrop) wantsDeemphasizedBackdrop;
@property (TB,N,GisAssistantAccessoryPresented,V_assistantAccessoryPresented) assistantAccessoryPresented;
@property (TB,N,GisEffectivelyVisionModality,V_effectivelyVisionModality) effectivelyVisionModality;
@property (TB,R,N,GisAnyAssistantPresentablePresented) anyAssistantPresentablePresented;
@property (TQ,R,N) modalities;
@property (TB,R,N) hasVoiceModality;
@property (TB,R,N) hasTextModality;
@property (TB,R,N) hasVisionModality;
```

## Instance methods

```
-[SBAssistantSessionPresentationContext setKeyboardVisible:];
-[SBAssistantSessionPresentationContext mutableCopyWithZone:];
-[SBAssistantSessionPresentationContext modalities];
-[SBAssistantSessionPresentationContext hash];
-[SBAssistantSessionPresentationContext isEqual:];
-[SBAssistantSessionPresentationContext isKeyboardVisible];
-[SBAssistantSessionPresentationContext hasTextModality];
-[SBAssistantSessionPresentationContext setAssistantAccessoryPresented:];
-[SBAssistantSessionPresentationContext allowsHDRContentBelow];
-[SBAssistantSessionPresentationContext hasVisionModality];
-[SBAssistantSessionPresentationContext hasVoiceModality];
-[SBAssistantSessionPresentationContext isAnyAssistantPresentablePresented];
-[SBAssistantSessionPresentationContext isAssistantAccessoryPresented];
-[SBAssistantSessionPresentationContext isAssistantPresented];
-[SBAssistantSessionPresentationContext isEffectivelyVisionModality];
-[SBAssistantSessionPresentationContext setAllowsHDRContentBelow:];
-[SBAssistantSessionPresentationContext setAssistantPresented:];
-[SBAssistantSessionPresentationContext setEffectivelyVisionModality:];
-[SBAssistantSessionPresentationContext setSiriPresentationOptions:];
-[SBAssistantSessionPresentationContext setWantsDeemphasizedBackdrop:];
-[SBAssistantSessionPresentationContext siriPresentationOptions];
-[SBAssistantSessionPresentationContext wantsDeemphasizedBackdrop];
```
