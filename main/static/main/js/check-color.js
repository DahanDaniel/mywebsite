function isDarkColor([r, g, b]) {
    // Calculate the brightness of the color
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
    return brightness < 128;
}
