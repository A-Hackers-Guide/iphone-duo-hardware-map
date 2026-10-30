# `TCArchetypeProfile`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSString" _conversationIdentifier;
@"NSArray" _frequentlyUsedAcronyms;
@"NSArray" _frequentlyUsedMessages;
@"NSString" _contractionUsage;
@"NSArray" _punctuationUsage;
@"NSArray" _nicknames;
@"TCArchetypeRelationship" _relationship;
@"NSArray" _intentBasedProfiles;
```

## Properties

```
@property (T@"NSString",&,N,V_conversationIdentifier) conversationIdentifier;
@property (T@"NSArray",&,N,V_frequentlyUsedAcronyms) frequentlyUsedAcronyms;
@property (T@"NSArray",&,N,V_frequentlyUsedMessages) frequentlyUsedMessages;
@property (T@"NSString",&,N,V_contractionUsage) contractionUsage;
@property (T@"NSArray",&,N,V_punctuationUsage) punctuationUsage;
@property (T@"NSArray",&,N,V_nicknames) nicknames;
@property (T@"TCArchetypeRelationship",&,N,V_relationship) relationship;
@property (T@"NSArray",&,N,V_intentBasedProfiles) intentBasedProfiles;
```

## Instance methods

```
-[TCArchetypeProfile setRelationship:];
-[TCArchetypeProfile conversationIdentifier];
-[TCArchetypeProfile setConversationIdentifier:];
-[TCArchetypeProfile relationship];
-[TCArchetypeProfile jsonString];
-[TCArchetypeProfile contractionUsage];
-[TCArchetypeProfile frequentlyUsedAcronyms];
-[TCArchetypeProfile frequentlyUsedMessages];
-[TCArchetypeProfile intentBasedProfiles];
-[TCArchetypeProfile nicknames];
-[TCArchetypeProfile punctuationUsage];
-[TCArchetypeProfile setNicknames:];
-[TCArchetypeProfile initWithConversationIdentifier:frequentlyUsedAcronyms:frequentlyUsedMessages:contractionUsage:punctuationUsage:nicknames:relationship:intentBasedProfiles:];
-[TCArchetypeProfile setContractionUsage:];
-[TCArchetypeProfile setFrequentlyUsedAcronyms:];
-[TCArchetypeProfile setFrequentlyUsedMessages:];
-[TCArchetypeProfile setIntentBasedProfiles:];
-[TCArchetypeProfile setPunctuationUsage:];
```
