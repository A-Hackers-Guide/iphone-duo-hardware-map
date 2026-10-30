# `TCTextCompositionInput`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"TCAttributedStringDigest" _digest;
@"NSAttributedString" _digestedAttributedString;
Q _offset;
@"NSDictionary" _filteredOptions;
@"TCTextCompositionUserProvidedPreferences" _userProvidedPreferences;
{_NSRange="location"Q"length"Q} _modifiedRange;
```

## Properties

```
@property (T@"NSString",R,C) string;
@property (T{_NSRange=QQ},R,V_modifiedRange) modifiedRange;
@property (TQ,R,V_offset) offset;
@property (T{_NSRange=QQ},R) actualRange;
@property (T{_NSRange=QQ},R) contextRange;
@property (T@"NSDictionary",R,C,V_filteredOptions) filteredOptions;
@property (T@"TCTextCompositionUserProvidedPreferences",R,C,V_userProvidedPreferences) userProvidedPreferences;
@property (T@"NSString",R,C) formattedString;
```

## Class methods

```
+[TCTextCompositionInput supportsSecureCoding];
```

## Instance methods

```
-[TCTextCompositionInput digest];
-[TCTextCompositionInput string];
-[TCTextCompositionInput encodeWithCoder:];
-[TCTextCompositionInput description];
-[TCTextCompositionInput initWithCoder:];
-[TCTextCompositionInput copyWithZone:];
-[TCTextCompositionInput offset];
-[TCTextCompositionInput formattedString];
-[TCTextCompositionInput contextRange];
-[TCTextCompositionInput filteredOptions];
-[TCTextCompositionInput actualRange];
-[TCTextCompositionInput digestedAttributedString];
-[TCTextCompositionInput formattedStringForRange:];
-[TCTextCompositionInput initForCompositionWithAttributedString:range:options:error:];
-[TCTextCompositionInput initWithAttributedString:range:options:error:];
-[TCTextCompositionInput initWithAttributedString:range:options:forComposition:lookBack:tagger:userProvidedPreferences:error:];
-[TCTextCompositionInput initWithAttributedString:range:options:lookBack:tagger:userProvidedPreferences:error:];
-[TCTextCompositionInput initWithAttributedString:range:options:userProvidedPreferences:error:];
-[TCTextCompositionInput initWithDigestedAttributedString:modifiedRange:offset:filteredOptions:userProvidedPreferences:];
-[TCTextCompositionInput initWithInput:additionalOptions:];
-[TCTextCompositionInput initWithInput:additionalOptions:userProvidedPreferences:];
-[TCTextCompositionInput modifiedRange];
-[TCTextCompositionInput userProvidedPreferences];
```
