# `TCAttributedSearchResultItem`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _isSelf;
@"NSString" _value;
@"NSString" _sourceBundleIdentifier;
@"NSString" _sourceItemIdentifier;
@"NSString" _contactLabel;
@"NSString" _attribute;
@"NSString" _contactName;
```

## Properties

```
@property (T@"NSString",R,C,N,V_value) value;
@property (T@"NSString",R,C,N,V_sourceBundleIdentifier) sourceBundleIdentifier;
@property (T@"NSString",R,C,N,V_sourceItemIdentifier) sourceItemIdentifier;
@property (T@"NSString",R,C,N,V_contactLabel) contactLabel;
@property (T@"NSString",R,C,N,V_attribute) attribute;
@property (TB,R,N,V_isSelf) isSelf;
@property (T@"NSString",R,C,N,V_contactName) contactName;
```

## Class methods

```
+[TCAttributedSearchResultItem supportsSecureCoding];
```

## Instance methods

```
-[TCAttributedSearchResultItem sourceItemIdentifier];
-[TCAttributedSearchResultItem sourceBundleIdentifier];
-[TCAttributedSearchResultItem contactLabel];
-[TCAttributedSearchResultItem value];
-[TCAttributedSearchResultItem contactName];
-[TCAttributedSearchResultItem encodeWithCoder:];
-[TCAttributedSearchResultItem hash];
-[TCAttributedSearchResultItem initWithCoder:];
-[TCAttributedSearchResultItem attribute];
-[TCAttributedSearchResultItem copyWithZone:];
-[TCAttributedSearchResultItem isEqual:];
-[TCAttributedSearchResultItem isSelf];
-[TCAttributedSearchResultItem initWithValue:sourceBundleIdentifier:sourceItemIdentifier:contactLabel:attribute:isSelf:contactName:];
```
