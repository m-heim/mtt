#![allow(unused)]

use clap::Parser;

/// Search for a pattern in a file and display the lines that contain it.
#[derive(Parser)]
struct Cli {
    /// The pattern to look for
    command: String,
    /// The path to the file to read
    path: std::path::PathBuf,
}

fn main() {
    println!("Thanks for using mtt! :)");
    let args = Cli::parse();
}
