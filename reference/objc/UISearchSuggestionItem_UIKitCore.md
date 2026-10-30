# `UISearchSuggestionItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualStyleStylable`, `UISearchSuggestion`
- 5 instance variables, 9 properties, 15 instance methods, 7 class methods

## Instance variables

```
@"NSAttributedString" _localizedAttributedSuggestion;
@"NSString" _localizedSuggestion;
@"NSString" _localizedDescription;
@"UIImage" _iconImage;
@ _representedObject;
```

## Properties

```
@property (T@"NSAttributedString",R,N,V_localizedAttributedSuggestion) localizedAttributedSuggestion;
@property (T@"NSString",R,N,V_localizedSuggestion) localizedSuggestion;
@property (T@"NSString",R,N,V_localizedDescription) localizedDescription;
@property (T@"UIImage",R,N,V_iconImage) iconImage;
@property (T@,&,N,V_representedObject) representedObject;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISearchSuggestionItem visualStyleRegistryIdentity];
+[UISearchSuggestionItem suggestionWithLocalizedAttributedSuggestion:];
+[UISearchSuggestionItem suggestionWithLocalizedAttributedSuggestion:descriptionString:];
+[UISearchSuggestionItem suggestionWithLocalizedAttributedSuggestion:descriptionString:iconImage:];
+[UISearchSuggestionItem suggestionWithLocalizedSuggestion:];
+[UISearchSuggestionItem suggestionWithLocalizedSuggestion:descriptionString:];
+[UISearchSuggestionItem suggestionWithLocalizedSuggestion:descriptionString:iconImage:];
```

## Instance methods

```
-[UISearchSuggestionItem localizedDescription];
-[UISearchSuggestionItem debugDescription];
-[UISearchSuggestionItem iconImage];
-[UISearchSuggestionItem hash];
-[UISearchSuggestionItem isEqual:];
-[UISearchSuggestionItem initWithLocalizedAttributedSuggestion:];
-[UISearchSuggestionItem initWithLocalizedAttributedSuggestion:localizedDescription:];
-[UISearchSuggestionItem initWithLocalizedAttributedSuggestion:localizedDescription:iconImage:];
-[UISearchSuggestionItem initWithLocalizedSuggestion:];
-[UISearchSuggestionItem initWithLocalizedSuggestion:localizedDescription:];
-[UISearchSuggestionItem initWithLocalizedSuggestion:localizedDescription:iconImage:];
-[UISearchSuggestionItem localizedAttributedSuggestion];
-[UISearchSuggestionItem localizedSuggestion];
-[UISearchSuggestionItem representedObject];
-[UISearchSuggestionItem setRepresentedObject:];
```
