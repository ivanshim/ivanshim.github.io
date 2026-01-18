# Morse-ESC

> **Morse-ESC** is a scalable binary transport over Morse timing in which values of arbitrary size are delimited solely by timing gaps, with only zero and the escape token treated specially.

*Envisioned by Ivan Shim and ChatGPT-5.2*  
*18 January 2026*

---

## 1. Purpose

Morse-ESC defines a minimal, extensible method for transmitting binary data over standard International Morse timing without redefining Morse symbols or introducing fixed-width encodings.

It enables arbitrarily large binary values to be conveyed using timing gaps as the sole framing mechanism, while preserving Morse code as a human-timed signaling layer.

---

## 2. Signaling Layer

Morse-ESC relies entirely on standard International Morse timing:

- Dot (`.`): 1 time unit  
- Dash (`-`): 3 time units  
- Intra-bit gap: 1 unit  
- Inter-value gap: 3 units  
- Inter-word gap: 7 units  

No additional symbols or timing rules are introduced.

---

## 3. Modes of Operation

Two interpretation modes exist:

- **Normal mode**: Signals are interpreted as standard International Morse Code.
- **Binary mode**: Signals are interpreted as binary values.

The system begins in normal mode.

---

## 4. Escape Token (ESC)

The sequence:

```
----
```


(four consecutive dashes, delimited by an inter-value gap) is reserved as the **ESC token**.

- In normal mode, a single `ESC` switches the decoder into binary mode.
- In binary mode, a single `ESC` switches the decoder back to normal mode.

The `ESC` token has no numeric meaning as a data value unless explicitly encoded as such (see Section 8).

---

## 5. Binary Alphabet

In binary mode:

- Dot (`.`) represents binary **0**
- Dash (`-`) represents binary **1**

Bits are transmitted most-significant-bit first.

---

## 6. Value Delimitation and Scalability

- A **binary value** is any non-empty sequence of bits (`.` and `-`).
- A value is terminated by an **inter-value gap** (3 units).
- There is **no fixed bit width**.
- Values may contain an arbitrary number of bits.

Value boundaries are determined solely by timing gaps.

---

## 7. Numeric Interpretation

- Binary values are interpreted as unsigned binary numbers.
- **Leading zero bits are permitted and discarded** during interpretation.
- **An all-zero value represents the binary value `0`.**

---

## 8. Special Handling of ESC as Data

The binary value corresponding to `ESC` is `1111`.

- A value consisting of exactly `1111` **with no leading zero bits** SHALL be interpreted as the **ESC control token**.
- The value `1111` SHALL be interpreted as a **literal data value** **only if it is prefixed with one or more leading zero bits**.

Examples:

```
---- → ESC (control)
.---- → ESC (data)
..---- → ESC (data)
...---- → ESC (data)
```

This rule removes all ambiguity between control and data representations of ESC.

---

## 9. ESC Control Semantics

At value boundaries:

- **One ESC token (`----`)**  
  → Toggle binary mode (enter if in normal mode, exit if in binary mode)

- **Two or more consecutive ESC tokens**  
  → **EXIT / ABORT / RESYNC**

Upon receiving two or more ESC tokens, the decoder SHALL:

- Immediately discard any partially received value
- Exit binary mode if active
- Return to normal Morse mode
- Reset parser state

No distinction is made between exit and abort; repetition of ESC unambiguously signals panic or resynchronization.

---

## 10. Token Recognition Rule

- ESC tokens are recognized **only at value boundaries**.
- Bit patterns occurring within a value are never interpreted as control tokens.

---

## 11. Error Handling

The following conditions are invalid:

- An empty value
- Any malformed timing that prevents value delimitation

On error, a decoder may resynchronize by waiting for a valid ESC sequence.

---

## 12. Architectural Interpretation

- Morse timing functions as the **physical and framing layer**.
- Normal Morse symbols form a **symbolic encoding layer**.
- Binary mode defines a **self-delimiting, arbitrarily scalable binary transport** over Morse timing.

Morse-ESC does not redefine International Morse Code; it overlays a reversible escape mechanism on top of it.

---

## 13. Scope and Intent

Morse-ESC is intended for experimentation, archival signaling, and machine-assisted decoding. It demonstrates that Morse timing alone is sufficient to support scalable data transport without expanding the Morse symbol table.

---

*End of document*
