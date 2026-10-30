# `UIPDFSelection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"UIPDFPage" _page;
^{CGPDFSelection=} _cgSelection;
B _dirty;
^{__CFString=} _string;
q _cachedStartIndex;
q _cachedEndIndex;
{?="location"q"length"q} stringRange;
```

## Properties

```
@property (T{?=qq},N,VstringRange) stringRange;
```

## Instance methods

```
-[UIPDFSelection startIndex];
-[UIPDFSelection archive];
-[UIPDFSelection init];
-[UIPDFSelection textAtIndex:];
-[UIPDFSelection dealloc];
-[UIPDFSelection string];
-[UIPDFSelection transform];
-[UIPDFSelection initWithSelection:];
-[UIPDFSelection endIndex];
-[UIPDFSelection isEmpty];
-[UIPDFSelection page];
-[UIPDFSelection bounds];
-[UIPDFSelection description];
-[UIPDFSelection extent];
-[UIPDFSelection CGSelection];
-[UIPDFSelection initWithPage:fromIndex:toIndex:];
-[UIPDFSelection setStringRange:];
-[UIPDFSelection attributedStringAtIndex:];
-[UIPDFSelection baseLineAtIndex:];
-[UIPDFSelection containingTextLine];
-[UIPDFSelection copyToPasteboard];
-[UIPDFSelection extendAtEnd:];
-[UIPDFSelection extendAtStart:];
-[UIPDFSelection extendToParagraph];
-[UIPDFSelection getBounds:transform:index:];
-[UIPDFSelection htmlAtIndex:];
-[UIPDFSelection initWithPage:cgSelection:];
-[UIPDFSelection initWithPage:fromArchive:];
-[UIPDFSelection isNonEmpty];
-[UIPDFSelection isWord];
-[UIPDFSelection numberOfRectangles];
-[UIPDFSelection rectangleAtIndex:scale:inset:];
-[UIPDFSelection selectionExtendedToLineBoundaries];
-[UIPDFSelection stringRange];
```
