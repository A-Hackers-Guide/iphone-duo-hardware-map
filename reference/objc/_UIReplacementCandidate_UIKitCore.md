# `_UIReplacementCandidate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 14 properties, 29 instance methods, 5 class methods

## Instance variables

```
B _isAutofillDoubleLineUI;
@"NSString" _documentTextToReplace;
@"NSString" _revertText;
@"NSArray" _alternativeRevertTexts;
@"NSArray" _candidateChoices;
@"NSArray" _underlines;
@"UITextRange" _rangeInDocument;
q _underlineStyle;
q _preferredPromptStyle;
q _preferredPromptButton;
@"NSNumber" _voiceCommandDisambiguationSelectedIndex;
@"NSUUID" _voiceCommandTrackingUUID;
@"NSNumber" _voiceCommandDisambiguationTargetCount;
```

## Properties

```
@property (T@"NSString",&,N,V_documentTextToReplace) documentTextToReplace;
@property (T@"NSString",&,N,V_revertText) revertText;
@property (T@"NSArray",&,N,V_alternativeRevertTexts) alternativeRevertTexts;
@property (T@"NSArray",&,N,V_candidateChoices) candidateChoices;
@property (T@"NSArray",&,N) textChoices;
@property (T@"NSArray",&,N,V_underlines) underlines;
@property (T@"UITextRange",&,N,V_rangeInDocument) rangeInDocument;
@property (Tq,N,V_underlineStyle) underlineStyle;
@property (Tq,N,V_preferredPromptStyle) preferredPromptStyle;
@property (Tq,N,V_preferredPromptButton) preferredPromptButton;
@property (T@"NSNumber",&,N,V_voiceCommandDisambiguationSelectedIndex) voiceCommandDisambiguationSelectedIndex;
@property (T@"NSUUID",&,N,V_voiceCommandTrackingUUID) voiceCommandTrackingUUID;
@property (T@"NSNumber",&,N,V_voiceCommandDisambiguationTargetCount) voiceCommandDisambiguationTargetCount;
@property (TB,N,V_isAutofillDoubleLineUI) isAutofillDoubleLineUI;
```

## Class methods

```
+[_UIReplacementCandidate candidateForAutocorrection:range:underlineStyle:promptStyle:promptButton:];
+[_UIReplacementCandidate candidateForAutocorrectionCandidate:range:];
+[_UIReplacementCandidate candidateForDocumentText:revertText:candidateChoices:range:underlineStyle:promptStyle:promptButton:];
+[_UIReplacementCandidate candidateForDocumentText:revertText:textChoices:range:underlineStyle:promptStyle:promptButton:];
+[_UIReplacementCandidate candidateForDocumentText:revertText:textChoices:range:underlineStyle:promptStyle:promptButton:voiceCommandDisambiguationSelectedIndex:voiceCommandDisambiguationTargetCount:];
```

## Instance methods

```
-[_UIReplacementCandidate initWithText:];
-[_UIReplacementCandidate documentTextToReplace];
-[_UIReplacementCandidate setDocumentTextToReplace:];
-[_UIReplacementCandidate rangeInDocument];
-[_UIReplacementCandidate setTextChoices:];
-[_UIReplacementCandidate alternativeRevertTexts];
-[_UIReplacementCandidate candidateChoices];
-[_UIReplacementCandidate isAutofillDoubleLineUI];
-[_UIReplacementCandidate preferredPromptButton];
-[_UIReplacementCandidate preferredPromptStyle];
-[_UIReplacementCandidate revertText];
-[_UIReplacementCandidate setAlternativeRevertTexts:];
-[_UIReplacementCandidate setCandidateChoices:];
-[_UIReplacementCandidate setIsAutofillDoubleLineUI:];
-[_UIReplacementCandidate setPreferredPromptButton:];
-[_UIReplacementCandidate setPreferredPromptStyle:];
-[_UIReplacementCandidate setRangeInDocument:];
-[_UIReplacementCandidate setRevertText:];
-[_UIReplacementCandidate setUnderlineStyle:];
-[_UIReplacementCandidate setUnderlines:];
-[_UIReplacementCandidate setVoiceCommandDisambiguationSelectedIndex:];
-[_UIReplacementCandidate setVoiceCommandDisambiguationTargetCount:];
-[_UIReplacementCandidate setVoiceCommandTrackingUUID:];
-[_UIReplacementCandidate textChoices];
-[_UIReplacementCandidate underlineStyle];
-[_UIReplacementCandidate underlines];
-[_UIReplacementCandidate voiceCommandDisambiguationSelectedIndex];
-[_UIReplacementCandidate voiceCommandDisambiguationTargetCount];
-[_UIReplacementCandidate voiceCommandTrackingUUID];
```
