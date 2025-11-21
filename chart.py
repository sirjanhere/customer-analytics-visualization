#!/usr/bin/env python3
"""
chart.py

Generates a professional Seaborn barplot showing average customer satisfaction
by product category and saves it as chart.png (512x512 pixels).

This script:
- creates realistic synthetic customer satisfaction data (scale 1-5)
- uses sns.barplot() to plot category means with standard-deviation error bars
- applies presentation-ready Seaborn styling and annotations
- saves the figure as a 512x512 PNG using figsize=(8,8) and dpi=64
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_synthetic_data(random_state: int = 2025) -> pd.DataFrame:
    """
    Generates realistic synthetic customer satisfaction scores (1-5)
    for a set of product categories. Each category has many customer
    ratings so the barplot shows meaningful averages with error bars.
    """
    rng = np.random.default_rng(random_state)

    categories = [
        "Electronics",
        "Home & Kitchen",
        "Clothing",
        "Sports & Outdoors",
        "Beauty",
        "Toys & Games",
        "Automotive",
    ]

    # baseline means for categories (on 1-5 scale), chosen to be realistic
    baseline_means = {
        "Electronics": 3.8,
        "Home & Kitchen": 4.1,
        "Clothing": 3.6,
        "Sports & Outdoors": 4.0,
        "Beauty": 4.3,
        "Toys & Games": 4.0,
        "Automotive": 3.7,
    }

    rows = []
    # create ~200 ratings per category with modest variance
    for cat in categories:
        mean = baseline_means[cat]
        # simulate individual customer responses with some skew and variance
        # use normal distribution then clip to [1,5]
        samples = rng.normal(loc=mean, scale=0.6, size=220)
        samples = np.clip(samples, 1.0, 5.0)
        for s in samples:
            rows.append({"Category": cat, "Satisfaction": s})

    df = pd.DataFrame(rows)
    return df

def create_barplot(df: pd.DataFrame, outpath: str = "chart.png") -> None:
    """
    Create a Seaborn barplot of average satisfaction by category and save PNG.
    The output image is exactly 512x512 pixels by using figsize=(8,8) and dpi=64.
    """
    # Styling for a professional, presentation-ready look
    sns.set_style("whitegrid")
    sns.set_context("talk", font_scale=1.05)
    plt.figure(figsize=(8, 8))  # 8in * 64dpi = 512px

    # Order categories by descending mean satisfaction for clearer storytelling
    order = df.groupby("Category")["Satisfaction"].mean().sort_values(ascending=False).index

    palette = sns.color_palette("crest", n_colors=len(order))

    ax = sns.barplot(
        data=df,
        x="Category",
        y="Satisfaction",
        order=order,
        palette=palette,
        ci="sd",       # show standard deviation as error bars
        capsize=0.08,  # small caps on error bars
    )

    # Set informative labels and title
    ax.set_title("Average Customer Satisfaction by Product Category", pad=14, fontsize=16, weight="semibold")
    ax.set_xlabel("")  # category names on x-axis are self-explanatory
    ax.set_ylabel("Average Satisfaction (1 = Poor, 5 = Excellent)", fontsize=12)

    # Show y axis range consistent with rating scale
    ax.set_ylim(1.0, 5.0)

    # Rotate x labels for readability
    plt.xticks(rotation=35, ha="right")

    # Annotate each bar with the mean value
    for p in ax.patches:
        height = p.get_height()
        x = p.get_x() + p.get_width() / 2
        ax.annotate(
            f"{height:.2f}",
            (x, height),
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="semibold",
            xytext=(0, 6),
            textcoords="offset points",
        )

    # Remove top/right spines for a cleaner look
    sns.despine(trim=False)

    plt.tight_layout()
    # Save to exactly 512x512 pixels
    plt.savefig(outpath, dpi=64, bbox_inches="tight")
    plt.close()

def main():
    df = generate_synthetic_data()
    create_barplot(df, outpath="chart.png")
    print("Saved chart.png (512x512)")

if __name__ == "__main__":
    main()