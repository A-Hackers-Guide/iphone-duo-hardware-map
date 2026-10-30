# `SBActivityItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"ACActivityContentUpdate" _contentUpdate;
@"NSString" _identifier;
d _relevanceScore;
@"ACActivityDescriptor" _descriptor;
```

## Properties

```
@property (T@"ACActivityContentUpdate",&,N,V_contentUpdate) contentUpdate;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"ACActivityDescriptor",R,N,V_descriptor) descriptor;
@property (Td,R,N,V_relevanceScore) relevanceScore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityItem descriptor];
-[SBActivityItem identifier];
-[SBActivityItem succinctDescriptionBuilder];
-[SBActivityItem relevanceScore];
-[SBActivityItem descriptionWithMultilinePrefix:];
-[SBActivityItem succinctDescription];
-[SBActivityItem description];
-[SBActivityItem isEqual:];
-[SBActivityItem descriptionBuilderWithMultilinePrefix:];
-[SBActivityItem contentUpdate];
-[SBActivityItem initWithContentUpdate:];
-[SBActivityItem setContentUpdate:];
```
