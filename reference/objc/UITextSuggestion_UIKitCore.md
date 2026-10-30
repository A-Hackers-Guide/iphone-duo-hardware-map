# `UITextSuggestion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputSuggestion`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 13 properties, 29 instance methods, 7 class methods

## Instance variables

```
B _displayStylePlain;
B _canDisplayInline;
@"NSString" _inputText;
@"NSString" _searchText;
@"NSString" _displayText;
@"NSString" _headerText;
@"UIImage" _image;
@"UIColor" _foregroundColor;
@"UIColor" _backgroundColor;
@"UIMenu" _menu;
Q _customInfoType;
@"NSUUID" _uuid;
```

## Properties

```
@property (T@"NSString",C,N,V_inputText) inputText;
@property (TQ,N,V_customInfoType) customInfoType;
@property (T@"TIKeyboardCandidate",R,N) _keyboardCandidate;
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T@"NSString",C,N,V_searchText) searchText;
@property (T@"NSString",C,N,V_displayText) displayText;
@property (T@"NSString",C,N,V_headerText) headerText;
@property (TB,N,V_displayStylePlain) displayStylePlain;
@property (T@"UIImage",C,N,V_image) image;
@property (T@"UIColor",C,N,V_foregroundColor) foregroundColor;
@property (T@"UIColor",C,N,V_backgroundColor) backgroundColor;
@property (TB,N,V_canDisplayInline) canDisplayInline;
@property (T@"UIMenu",&,N,V_menu) menu;
```

## Class methods

```
+[UITextSuggestion supportsSecureCoding];
+[UITextSuggestion classFallbacksForKeyedArchiver];
+[UITextSuggestion decodeTextSuggestions:];
+[UITextSuggestion encodeTextSuggestions:];
+[UITextSuggestion textSuggestionWithInputText:];
+[UITextSuggestion textSuggestionWithInputText:searchText:];
+[UITextSuggestion textSuggestionWithInputText:searchText:customInfoType:];
```

## Instance methods

```
-[UITextSuggestion menu];
-[UITextSuggestion setForegroundColor:];
-[UITextSuggestion setDisplayText:];
-[UITextSuggestion uuid];
-[UITextSuggestion setCustomInfoType:];
-[UITextSuggestion init];
-[UITextSuggestion headerText];
-[UITextSuggestion searchText];
-[UITextSuggestion customInfoType];
-[UITextSuggestion setInputText:];
-[UITextSuggestion setBackgroundColor:];
-[UITextSuggestion setSearchText:];
-[UITextSuggestion encodeWithCoder:];
-[UITextSuggestion inputText];
-[UITextSuggestion backgroundColor];
-[UITextSuggestion displayText];
-[UITextSuggestion initWithCoder:];
-[UITextSuggestion image];
-[UITextSuggestion foregroundColor];
-[UITextSuggestion copyWithZone:];
-[UITextSuggestion setMenu:];
-[UITextSuggestion setImage:];
-[UITextSuggestion _keyboardCandidate];
-[UITextSuggestion canDisplayInline];
-[UITextSuggestion displayStylePlain];
-[UITextSuggestion initWithInputText:searchText:displayText:headerText:customInfoType:];
-[UITextSuggestion setCanDisplayInline:];
-[UITextSuggestion setDisplayStylePlain:];
-[UITextSuggestion setHeaderText:];
```
