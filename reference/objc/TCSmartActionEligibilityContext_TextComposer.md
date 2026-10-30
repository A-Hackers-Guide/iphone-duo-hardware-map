# `TCSmartActionEligibilityContext`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
q _conversationState;
@"TCInputContextHistory" _inputContextHistory;
@"NSArray" _messagesInLookbackWindow;
@"NSDictionary" _options;
@"NSString" _detectedLanguage;
```

## Properties

```
@property (Tq,R,N,V_conversationState) conversationState;
@property (T@"TCInputContextHistory",R,C,N,V_inputContextHistory) inputContextHistory;
@property (T@"NSArray",R,C,N,V_messagesInLookbackWindow) messagesInLookbackWindow;
@property (T@"NSDictionary",R,C,N,V_options) options;
@property (T@"NSString",R,C,N,V_detectedLanguage) detectedLanguage;
```

## Instance methods

```
-[TCSmartActionEligibilityContext inputContextHistory];
-[TCSmartActionEligibilityContext detectedLanguage];
-[TCSmartActionEligibilityContext conversationState];
-[TCSmartActionEligibilityContext options];
-[TCSmartActionEligibilityContext initWithConversationState:inputContextHistory:messagesInLookbackWindow:options:detectedLanguage:];
-[TCSmartActionEligibilityContext messagesInLookbackWindow];
```
