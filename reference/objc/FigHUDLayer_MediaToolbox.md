# `FigHUDLayer`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 7 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{__CTFont=} _Font;
d _FontSize;
^{__CFDictionary=} _TextAttributes;
^{__CFArray=} _Labels;
^{__CFArray=} _Values;
^{__CFArray=} _LabelColors;
^{__CFArray=} _ValueColors;
```

## Instance methods

```
-[FigHUDLayer setValue:atIndex:];
-[FigHUDLayer drawInContext:];
-[FigHUDLayer init];
-[FigHUDLayer dealloc];
-[FigHUDLayer addLine:withColorIndex:];
-[FigHUDLayer addLine:withLabelColorIndex:withValueColorIndex:];
-[FigHUDLayer getLabels];
-[FigHUDLayer getValues];
-[FigHUDLayer resetLines];
-[FigHUDLayer setFont:withPointSize:];
-[FigHUDLayer setValueAtIndex:format:];
```
