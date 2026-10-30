# `AVCaption`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 1 instance variables, 3 properties, 40 instance methods, 3 class methods

## Instance variables

```
@"AVCaptionInternal" _internal;
```

## Properties

```
@property (T^{OpaqueFigCaptionData=},R,N) _figCaptionData;
@property (T@"NSString",R,N) text;
@property (T{?={?=qiIq}{?=qiIq}},R,N) timeRange;
```

## Class methods

```
+[AVCaption supportsSecureCoding];
+[AVCaption _appendFigStyleKey:value:range:toArray:];
+[AVCaption captionFromFigCaption:];
```

## Instance methods

```
-[AVCaption region];
-[AVCaption mutableCopyWithZone:];
-[AVCaption timeRange];
-[AVCaption textAlignment];
-[AVCaption text];
-[AVCaption init];
-[AVCaption dealloc];
-[AVCaption encodeWithCoder:];
-[AVCaption description];
-[AVCaption initWithCoder:];
-[AVCaption copyWithZone:];
-[AVCaption animation];
-[AVCaption _setRegion:];
-[AVCaption _figCaptionData];
-[AVCaption _setAnimation:];
-[AVCaption _setBackgroundColor:inRange:];
-[AVCaption _setDecoration:inRange:];
-[AVCaption _setFontStyle:inRange:];
-[AVCaption _setFontWeight:inRange:];
-[AVCaption _setRuby:inRange:];
-[AVCaption _setStylePropertiesForArchive:];
-[AVCaption _setText:];
-[AVCaption _setTextAlignment:];
-[AVCaption _setTextColor:inRange:];
-[AVCaption _setTextCombine:inRange:];
-[AVCaption _setTimeRange:];
-[AVCaption _stylePropertiesForArchive];
-[AVCaption backgroundColorAtIndex:range:];
-[AVCaption copyBackgroundColorAtIndex:range:];
-[AVCaption copyTextColorAtIndex:range:];
-[AVCaption decorationAtIndex:range:];
-[AVCaption fontStyleAtIndex:range:];
-[AVCaption fontWeightAtIndex:range:];
-[AVCaption initWithFigCaptionData:timeRange:];
-[AVCaption initWithFigMutableCaptionData:timeRange:];
-[AVCaption initWithText:timeRange:];
-[AVCaption rubyAtIndex:range:];
-[AVCaption rubyTextAtIndex:range:];
-[AVCaption textColorAtIndex:range:];
-[AVCaption textCombineAtIndex:range:];
```
