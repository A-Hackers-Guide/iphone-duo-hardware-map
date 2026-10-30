# `TCSmartReplyUserQuestionnaireEntry`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _answerOptionsArray;
@"NSString" _question;
@"NSString" _selectedOption;
@"NSString" _defaultOption;
```

## Properties

```
@property (T@"NSString",R,C,N,V_question) question;
@property (T@"NSOrderedSet",R,C,N) answerOptions;
@property (T@"NSString",R,C,N,V_selectedOption) selectedOption;
@property (T@"NSString",R,C,N,V_defaultOption) defaultOption;
```

## Class methods

```
+[TCSmartReplyUserQuestionnaireEntry supportsSecureCoding];
```

## Instance methods

```
-[TCSmartReplyUserQuestionnaireEntry defaultOption];
-[TCSmartReplyUserQuestionnaireEntry selectedOption];
-[TCSmartReplyUserQuestionnaireEntry encodeWithCoder:];
-[TCSmartReplyUserQuestionnaireEntry hash];
-[TCSmartReplyUserQuestionnaireEntry description];
-[TCSmartReplyUserQuestionnaireEntry initWithCoder:];
-[TCSmartReplyUserQuestionnaireEntry copyWithZone:];
-[TCSmartReplyUserQuestionnaireEntry isEqual:];
-[TCSmartReplyUserQuestionnaireEntry question];
-[TCSmartReplyUserQuestionnaireEntry answerOptions];
-[TCSmartReplyUserQuestionnaireEntry initWithAnswerOptions:question:selectedOption:defaultOption:];
-[TCSmartReplyUserQuestionnaireEntry initWithAnswerOptionsArray:question:selectedOption:defaultOption:];
```
